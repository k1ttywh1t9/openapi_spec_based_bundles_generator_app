from collections.abc import Iterable
from dataclasses import dataclass

from domain.entities.resources import APIResource, APIResourcesBundle
from logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateAPIResourcesFromSpecCommand(BaseCommand): ...


@dataclass(frozen=True)
class CreateAPIResourcesBundleFromSpecCommandHandler(
    CommandHandler[CreateAPIResourcesFromSpecCommand, APIResource]
):
    async def handle(self, command: CreateAPIResourcesFromSpecCommand) -> APIResourcesBundle:
        ...
