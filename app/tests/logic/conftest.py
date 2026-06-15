import pytest_asyncio

from tests.logic.conftest import *  # noqa
import pytest
import orjson
from typing import Container

from domain.entities.specs import OpenAPISpec
from infra.message_brokers.base import BaseMessageBroker
from logic.commands.specs import CreateNewOpenAPISpecEntityFromRawCommand
from logic.mediator.main import Mediator
from settings.main import Settings


def load_openapi_file(path) -> dict:
    with open(path, "rb") as f:
        return orjson.loads(f.read())


@pytest_asyncio.fixture(params=["memory", "file"])
async def parsed_spec(request, container: Container) -> OpenAPISpec:
    """Step 1 Fixture: Create spec from various sources.

    1. From memory
    2. From file
    """
    mediator: Mediator = container.resolve(Mediator)
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    settings: Settings = container.resolve(Settings)

    await message_broker.start()

    if request.param == "memory":
        title = "Pet Care API"
        data = {"openapi": "3.0.0", "info": {"title": "Petstore"}}

    elif request.param == "file":
        data = load_openapi_file(path=settings.openapi.path)
        title = "Real Petstore File API"

    else:
        raise ValueError(f"Unknown spec source: {request.param}")

    command = CreateNewOpenAPISpecEntityFromRawCommand(title=title, data=data)
    results = await mediator.handle_command(command)

    return list(results)[0]
