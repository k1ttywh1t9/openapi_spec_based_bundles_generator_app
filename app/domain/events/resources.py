from dataclasses import dataclass
from typing import ClassVar

from domain.events.base import BaseEvent


@dataclass
class NewAPIResourceCreatedEvent(BaseEvent):
    title: ClassVar[str] = "New API Resource Created"

    api_resource_oid: str


@dataclass
class NewUIResourceCreatedEvent(BaseEvent):
    title: ClassVar[str] = "New UI Resource Created"

    ui_resource_oid: str
