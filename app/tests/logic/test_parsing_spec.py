import orjson
import pytest
from punq import Container
from domain.entities.specs import OpenAPISpec
from infra.message_brokers.base import BaseMessageBroker
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from logic.commands.specs import ParseOpenAPISpecToEntityCommand
from logic.mediator.main import Mediator


@pytest.mark.asyncio
async def test_parse_openapi_spec_to_entity_logic_success(container: Container):
    mediator: Mediator = container.resolve(Mediator)
    openapi_specs_repo: BaseOpenAPISpecsRepository = container.resolve(
        BaseOpenAPISpecsRepository
    )
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)

    await message_broker.start()

    test_title = "Pet Care API"
    test_data = {"openapi": "3.0.0", "info": {"title": "Petstore"}}

    command = ParseOpenAPISpecToEntityCommand(title=test_title, data=test_data)

    results = await mediator.handle_command(command)
    results_list = list(results)

    assert (
        len(results_list) == 1
    ), "Only one handler command handler have to be interacted"
    returned_spec = results_list[0]
    assert isinstance(returned_spec, OpenAPISpec)
    assert returned_spec.title.value == test_title

    saved_spec = await openapi_specs_repo.get_item_by_oid(returned_spec.oid)
    assert saved_spec is not None, "Specification have to be saved in repository"
    assert saved_spec.oid == returned_spec.oid

    sent_messages = message_broker._topics["openapi_specifications_topic"]

    assert len(sent_messages) == 1, "Integration event have to be sent to broker"

    payload = orjson.loads(sent_messages[0])
    assert "event_id" in payload
    assert payload["spec_oid"] == returned_spec.oid

    # # --- НАЧАЛО ТЕСТИРОВАНИЯ ШАГА 2 ---
    # bundle_repo = container.resolve(BaseAPIResourcesBundleRepository)

    # # 1. Настраиваем и запускаем фоновый воркер
    # from logic.worker import run_specs_worker
    # await run_specs_worker(broker=message_broker, mediator=mediator)

    # # 2. Так как наш MemoryMessageBroker при вызове send_message в Шаге 1
    # # сразу же триггерит подписчиков, цепочка Шага 2 уже должна выполниться!

    # # 3. Проверяем, что бандл ресурсов создался и сохранился в репозиторий
    # all_bundles = list(await bundle_repo.get_all_items(filters=any_filter_or_mock))
    # assert len(all_bundles) == 1, "Бандл ресурсов должен автоматически создаться воркером"

    # saved_bundle = all_bundles[0]
    # assert saved_bundle.spec_oid == returned_spec.oid
