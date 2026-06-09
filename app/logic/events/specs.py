from dataclasses import dataclass

from domain.events.specs import NewOpenAPISpecEntityCreatedEvent
from logic.events.base import EventHandler
from logic.events.converters import convert_event_to_broker_message


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
