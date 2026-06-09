from functools import lru_cache

from punq import Container, Scope

from domain.events.specs import NewOpenAPISpecEntityCreatedEvent
from infra.message_brokers.base import BaseMessageBroker
from infra.message_brokers.memory import MemoryMessageBroker
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from infra.repositories.specs.memory import MemoryOpenAPISpecRepository
from logic.commands.specs import (
    ParseOpenAPISpecToEntityCommand,
    ParseOpenAPISpecToEntityCommandHandler,
)
from logic.events.specs import NewOpenAPISpecEntityCreatedEventHandler
from logic.mediator.main import Mediator
from settings.main import Settings


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    # Main Settings
    container.register(Settings, instance=Settings(), scope=Scope.singleton)
    settings: Settings = container.resolve(Settings)

    # Repositories
    container.register(
        BaseOpenAPISpecsRepository,
        MemoryOpenAPISpecRepository,
        scope=Scope.singleton,
    )

    # Message Brokers
    def create_message_broker() -> BaseMessageBroker:
        return MemoryMessageBroker()

    container.register(
        BaseMessageBroker,
        factory=create_message_broker,
        scope=Scope.singleton,
    )

    # Handlers
    container.register(ParseOpenAPISpecToEntityCommandHandler)
    container.register(NewOpenAPISpecEntityCreatedEventHandler)

    # Mediator
    def init_mediator(container: Container) -> Mediator:
        mediator = Mediator()

        parse_openapi_command_handler = ParseOpenAPISpecToEntityCommandHandler(
            _mediator=mediator,
            specs_repository=container.resolve(BaseOpenAPISpecsRepository),
        )
        new_openapi_entity_event_handler = NewOpenAPISpecEntityCreatedEventHandler(
            message_broker=container.resolve(BaseMessageBroker),
            broker_topic="openapi_specifications_topic",
        )

        # punq will extract BaseOpenAPISpecsRepository and Mediator from container and send to handler
        mediator.register_command(
            ParseOpenAPISpecToEntityCommand,
            [parse_openapi_command_handler],
        )

        mediator.register_event(
            NewOpenAPISpecEntityCreatedEvent,
            [new_openapi_entity_event_handler],
        )

        return mediator

    container.register(
        Mediator,
        factory=lambda: init_mediator(container),
        scope=Scope.singleton,
    )

    return container
