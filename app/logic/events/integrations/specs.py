from dataclasses import dataclass
from typing import ClassVar

from logic.commands.resources import CreateAPIResourcesBundleFromSpecCommand
from logic.events.integrations.base import IntegrationEvent, IntegrationEventHandler


@dataclass
class OpenAPISpecEntityReceivedFromBrokerEvent(IntegrationEvent):
    event_title: ClassVar[str] = "New OpenAPI Spec Received From Broker"
    spec_oid: str


@dataclass
class OpenAPISpecEntityReceivedFromBrokerEventHandler(
    IntegrationEventHandler[OpenAPISpecEntityReceivedFromBrokerEvent, None]
):
    async def handle(self, event: OpenAPISpecEntityReceivedFromBrokerEvent) -> None:
        command = CreateAPIResourcesBundleFromSpecCommand(spec_oid=event.spec_oid)
        await self._mediator.handle_command(command)
