from punq import Container, Scope

from logic.mediator.main import Mediator
from settings.main import Settings


def _init_container() -> Container:
    container = Container()

    # init main settings
    container.register(Settings, instance=Settings(), scope=Scope.singletone)

    settings: Settings = container.resolve(Settings)

    # Mediator
    def init_mediator() -> Mediator:
        mediator = Mediator()

        # event handlers

        # command handlers

        # Events

        # Commands

        return mediator

    container.register(Mediator, factory=init_mediator)

    return container
