import pathlib
from typing import Container

import orjson
import pytest

from domain.entities.specs import OpenAPISpec
from infra.message_brokers.base import BaseMessageBroker
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from logic.commands.specs import CreateNewOpenAPISpecEntityFromRawCommand
from logic.mediator.main import Mediator
from settings.main import Settings


def load_openapi_file(path: str) -> dict:
    if not path.exists():
        pytest.fail(f"File not found: {path}")

    with open(path, "rb") as f:
        return orjson.loads(f.read())


@pytest.mark.asyncio
async def test_parsing_openapi_spec_to_entity_from_file_logic_success(
    container: Container,
):
    # 1. Arrange: Вытаскиваем инфраструктуру из DI-контейнера
    mediator: Mediator = container.resolve(Mediator)
    repository: BaseOpenAPISpecsRepository = container.resolve(
        BaseOpenAPISpecsRepository
    )
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    settings: Settings = container.resolve(Settings)

    await message_broker.start()

    # Загружаем реальные данные из файла
    real_spec_data = load_openapi_file(
        path=settings.openapi.path,
    )
    title = "Real Petstore File API"

    # Формируем команду с настоящей "жирной" схемой
    command = CreateNewOpenAPISpecEntityFromRawCommand(
        title=title,
        data=real_spec_data,
    )

    # 2. Act: Запускаем команду через медиатор
    results = await mediator.handle_command(command)
    results_list = list(results)

    # 3. Assertions
    # Проверяем, что сущность успешно создалась из сложных данных
    assert len(results_list) == 1
    entity = results_list[0]
    assert isinstance(entity, OpenAPISpec)
    assert entity.title.value == title

    assert entity.data["info"]["title"] == real_spec_data["info"]["title"]

    # Проверяем, что в репозиторий сохранился именно наш реальный json
    spec_from_storage = await repository.get_item_by_oid(entity.oid)
    assert spec_from_storage is not None
    assert (
        spec_from_storage.data["info"]["version"] == real_spec_data["info"]["version"]
    )

    # Проверяем интеграционное событие в брокере сообщений
    topic = settings.message_broker.topics.new_openapi_spec_entity_created_topic
    broker_messages = message_broker._topics[topic]
    assert len(broker_messages) == 1

    payload = orjson.loads(broker_messages[0])
    assert "event_id" in payload
    assert payload["spec_oid"] == entity.oid
