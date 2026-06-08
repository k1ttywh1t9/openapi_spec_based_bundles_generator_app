from dataclasses import dataclass
from typing import ClassVar


from domain.events.base import BaseEvent
from domain.events.messages import (
    NewChatCreatedEvent,
)
from domain.events.specs import NewOpenAPISpecEntityCreatedEvent
from infra.message_brokers.converters import convert_event_to_broker_message
from logic.events.base import (
    EventHandler,
    IntegrationEvent,
)


@dataclass
class NewOpenAPISpecEntityCreatedEventHandler(
    EventHandler[NewOpenAPISpecEntityCreatedEvent, None]
):

    async def handle(self, event: NewOpenAPISpecEntityCreatedEvent) -> None:
        await self.message_broker.send_message(
            topic=self.broker_topic,
            value=convert_event_to_broker_message(event=event),
            key=str(event.event_id).encode(),
        )


@dataclass
class NewMessageReceivedEventHandler(EventHandler[NewMessageReceivedEvent, None]):
    async def handle(self, event: NewMessageReceivedEvent) -> None:
        await self.message_broker.send_message(
            topic=self.broker_topic,
            value=convert_event_to_broker_message(event=event),
            key=event.chat_oid.encode(),
        )


@dataclass
class NewOpenAPISpecReceivedFromAPIEvent(IntegrationEvent):
    event_title: ClassVar[str] = "New OpenAPI Spec Received From API"

    openapi_spec_oid: str


@dataclass
class NewOpenAPISpecReceivedFromFileEvent(IntegrationEvent):
    event_title: ClassVar[str] = "New OpenAPI Spec Received From File"

    openapi_spec_oid: str


@dataclass
class NewOpenAPISpecReceivedFromBrokerEvent(IntegrationEvent):
    event_title: ClassVar[str] = "New OpenAPI Spec Received From Broker"

    openapi_spec_oid: str
