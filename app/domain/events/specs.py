from dataclasses import dataclass
from typing import ClassVar

from domain.events.base import BaseEvent


@dataclass
class NewOpenAPISpecEntityCreatedEvent(BaseEvent):
    event_title: ClassVar[str] = "New OpenAPI Spec Entity Created"

    openapi_spec_oid: str
