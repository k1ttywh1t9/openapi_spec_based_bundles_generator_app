from typing import Container

import orjson
import pytest

from domain.entities.specs import OpenAPISpec
from infra.message_brokers.base import BaseMessageBroker
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from logic.commands.specs import CreateNewOpenAPISpecEntityFromRawCommand
from logic.mediator.main import Mediator
from settings.main import Settings


def get_test_data() -> dict:
    title = "Pet Care API"
    data = {"openapi": "3.0.0", "info": {"title": "Petstore"}}
    payload = {
        "title": title,
        "data": data,
    }
    return payload


@pytest.mark.asyncio
async def test_parsing_openapi_spec_to_entity_from_memory_logic_success(
    container: Container,
):
    mediator: Mediator = container.resolve(Mediator)
    repository: BaseOpenAPISpecsRepository = container.resolve(
        BaseOpenAPISpecsRepository
    )
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    settings: Settings = container.resolve(Settings)

    await message_broker.start()

    title = get_test_data().get("title")
    data = get_test_data().get("data")

    command = CreateNewOpenAPISpecEntityFromRawCommand(
        title=title,
        data=data,
    )

    results = await mediator.handle_command(command)
    results_list = list(results)

    # assertions
    # entity
    assert len(results_list) == 1
    entity = results_list[0]
    assert isinstance(entity, OpenAPISpec)
    assert entity.title.value == title

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


