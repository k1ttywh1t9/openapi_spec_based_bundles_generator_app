from dataclasses import dataclass
from typing import ClassVar

from domain.events.base import BaseEvent


@dataclass
class NewOpenAPISpecReceivedEvent(BaseEvent):
    event_title: ClassVar[str] = "New OpenAPI specification received"

    openapi_spec_oid: str
