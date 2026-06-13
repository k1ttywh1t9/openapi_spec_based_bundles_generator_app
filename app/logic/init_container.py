from functools import lru_cache

from punq import Container, Scope

from infra.message_brokers.base import BaseMessageBroker
from infra.message_brokers.memory import MemoryMessageBroker
from infra.repositories.resources.base import (
    BaseAPIResourcesBundlesRepository,
    BaseAPIResourcesRepository,
)
from infra.repositories.resources.memory import (
    MemoryAPIResourcesBundleRepository,
    MemoryAPIResourcesRepository,
)
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from infra.repositories.specs.memory import MemoryOpenAPISpecRepository
from logic.commands.resources import CreateAPIResourcesBundleFromSpecCommandHandler
from logic.commands.specs import (
    CreateNewOpenAPISpecEntityFromRawCommandHandler,
)
from logic.events.domain.specs import NewOpenAPISpecEntityCreatedFromRawEventHandler
from logic.events.integrations.specs import OpenAPISpecEntityReceivedFromBrokerEventHandler
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
    container.register(
        BaseAPIResourcesRepository,
        MemoryAPIResourcesRepository,
        scope=Scope.singleton,
    )
    container.register(
        BaseAPIResourcesBundlesRepository,
        MemoryAPIResourcesBundleRepository,
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
    # Step 1
    container.register(CreateNewOpenAPISpecEntityFromRawCommandHandler)
    container.register(NewOpenAPISpecEntityCreatedFromRawEventHandler)

    # Step 2
    container.register(OpenAPISpecEntityReceivedFromBrokerEventHandler)
    container.register(CreateAPIResourcesBundleFromSpecCommandHandler)

    # Mediator
    def init_mediator(container: Container) -> Mediator:
        mediator = Mediator()

        create_new_openapi_spec_entity_from_raw_command_handler = (
            CreateNewOpenAPISpecEntityFromRawCommandHandler(
                _mediator=mediator,
                specs_repository=container.resolve(BaseOpenAPISpecsRepository),
            )
        )
        new_openapi_spec_entity_created_from_raw_event_handler = NewOpenAPISpecEntityCreatedFromRawEventHandler(
            message_broker=container.resolve(BaseMessageBroker),
            broker_topic=settings.message_broker.topics.new_openapi_spec_entity_created_topic,
        )
        openapi_spec_entity_received_from_broker_event_handler = (
            OpenAPISpecEntityReceivedFromBrokerEventHandler(
                _mediator=mediator,
            )
        )
        create_api_resources_bundle_from_spec_command_handler = (
            CreateAPIResourcesBundleFromSpecCommandHandler(
                _mediator=mediator,
                specs_repository=container.resolve(BaseOpenAPISpecsRepository),
                bundles_repository=container.resolve(BaseAPIResourcesBundlesRepository),
            )
        )

        mediator.register_command(
            command=CreateNewOpenAPISpecEntityFromRawCommandHandler,
            command_handlers=[
                create_new_openapi_spec_entity_from_raw_command_handler,
            ],
        )

        mediator.register_event(
            event=NewOpenAPISpecEntityCreatedFromRawEventHandler,
            event_handlers=[
                new_openapi_spec_entity_created_from_raw_event_handler,
            ],
        )

        mediator.register_command(
            command=OpenAPISpecEntityReceivedFromBrokerEventHandler,
            command_handlers=[
                openapi_spec_entity_received_from_broker_event_handler,
            ],
        )

        mediator.register_event(
            event=CreateAPIResourcesBundleFromSpecCommandHandler,
            event_handlers=[
                create_api_resources_bundle_from_spec_command_handler,
            ],
        )

        return mediator

    container.register(
        Mediator,
        factory=lambda: init_mediator(container),
        scope=Scope.singleton,
    )

    return container
