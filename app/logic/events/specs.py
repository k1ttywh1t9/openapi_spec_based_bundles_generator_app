from dataclasses import dataclass
from typing import ClassVar

from app.domain.events.specs import NewOpenAPISpecReceivedEvent
from domain.events.messages import (
    NewChatCreatedEvent,
    NewMessageReceivedEvent,
)
from infra.message_brokers.converters import convert_event_to_broker_message
from logic.events.base import (
    EventHandler,
    IntegrationEvent,
)


@dataclass
class NewOpenAPISpecReceivedEventHandler(
    EventHandler[NewOpenAPISpecReceivedEvent, None]
):
    async def handle(self, event: NewMessageReceivedEvent) -> None:
        ...
        # await self.message_broker.send_message(
        #     topic=self.broker_topic,
        #     value=convert_event_to_broker_message(event=event),
        #     key=event.chat_oid.encode(),
        # )


@dataclass
class NewOpenAPISpecReceivedEvent(BaseEvent):
    event_title: ClassVar[str] = "New OpenAPI Spec Received"

    openapi_spec_oid: str
