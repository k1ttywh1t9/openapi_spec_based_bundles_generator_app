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


def _init_container() -> Container:
    container = Container()

    # Main Settings
    container.register(Settings, instance=Settings(), scope=Scope.singletone)
    settings: Settings = container.resolve(Settings)

    # Repositories
    container.register(
        BaseOpenAPISpecsRepository,
        MemoryOpenAPISpecRepository,
        scope=Scope.singleton,
    )

    # Message Brokers
    container.register(
        BaseMessageBroker,
        MemoryMessageBroker,
        scope=Scope.singleton,
    )

    # Handlers
    container.register(ParseOpenAPISpecToEntityCommandHandler)
    container.register(NewOpenAPISpecEntityCreatedEventHandler)

    # Mediator
    def init_mediator() -> Mediator:
        mediator = Mediator()

        # punq will extract BaseOpenAPISpecsRepository and Mediator from container and send to handler
        mediator.register_command(
            ParseOpenAPISpecToEntityCommand,
            [container.resolve(ParseOpenAPISpecToEntityCommandHandler)],
        )

        mediator.register_event(
            NewOpenAPISpecEntityCreatedEvent,
            [container.resolve(NewOpenAPISpecEntityCreatedEventHandler)],
        )

        return mediator

    container.register(Mediator, factory=init_mediator, scope=Scope.singleton)

    return container
