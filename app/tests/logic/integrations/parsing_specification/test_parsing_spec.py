from typing import Container

import orjson
import pytest

from domain.entities.specs import OpenAPISpec
from infra.message_brokers.base import BaseMessageBroker
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from settings.main import Settings


@pytest.mark.asyncio
async def test_parsing_openapi_spec_to_entity_logic_success(
    parsed_spec: OpenAPISpec,
    container: Container,
):
    """Тест проверяет, что сущность корректно создана, сохранена в репозиторий
    и событие улетело в брокер (работает для всех типов источников через фикстуру).
    """
    repository: BaseOpenAPISpecsRepository = container.resolve(
        BaseOpenAPISpecsRepository
    )
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    settings: Settings = container.resolve(Settings)

    # assertions
    # entity
    entity = [parsed_spec]
    assert isinstance(entity, OpenAPISpec)
    # assert entity.title.value == title

    # storage
    spec_from_storage = await repository.get_item_by_oid(entity.oid)
    assert spec_from_storage is not None
    assert spec_from_storage.oid == entity.oid

    # broker
    topic = settings.message_broker.topics.new_openapi_spec_entity_created_topic
    broker_messages = message_broker._topics[topic]
    assert len(broker_messages) == 1
    payload = orjson.loads(broker_messages[0])
    assert "event_id" in payload
    assert payload["spec_oid"] == entity.oid
