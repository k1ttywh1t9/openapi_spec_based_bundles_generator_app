from dataclasses import dataclass
from typing import ClassVar

from domain.events.base import BaseEvent


@dataclass
class NewAPIResourceCreatedEvent(BaseEvent):
    event_title: ClassVar[str] = "New API resource created"

    api_resource_oid: str
    api_resource_title: str


@dataclass
class NewAPIResourcesBundleCreatedEvent(BaseEvent):
    event_title: ClassVar[str] = "New Bundle of API resources created"

    bundle_oid: str
    bundle_title: str


@dataclass
class NewControllerResourceCreatedEvent(BaseEvent):
    event_title: ClassVar[str] = "New controller resource created"

    controller_resource_oid: str


@dataclass
class NewViewResourceCreatedEvent(BaseEvent):
    event_title: ClassVar[str] = "New view resource created"

    view_resource_oid: str


@dataclass
class NewMVCResourceCreatedEvent(BaseEvent):
    event_title: ClassVar[str] = "New MVC resource created"

    mvc_resource_oid: str
    mvc_resource_title: str


@dataclass
class NewMVCResourcesBundleCreatedEvent(BaseEvent):
    title: ClassVar[str] = "Created new bundle with MVC recources"

    chat_oid: str
    chat_title: str
