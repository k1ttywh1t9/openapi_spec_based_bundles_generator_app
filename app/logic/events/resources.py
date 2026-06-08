from dataclasses import dataclass

from domain.events.resources import NewAPIResourceCreatedEvent
from logic.events.base import EventHandler


@dataclass
class NewAPIResourceCreatedEventHandler(EventHandler[NewAPIResourceCreatedEvent, None]):
    async def handle(self, event: NewAPIResourceCreatedEvent) -> None:
        ...


@dataclass
class NewAPIResourcesBundleCreatedEventHandler(EventHandler[NewAPIResourceCreatedEvent, None]):
    bundle_oid: str
    
    async def handle(self, event: NewAPIResourceCreatedEvent) -> None: ...
