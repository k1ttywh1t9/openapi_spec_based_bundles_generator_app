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
