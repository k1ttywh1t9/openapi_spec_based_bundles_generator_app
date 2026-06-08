from dataclasses import dataclass

from domain.entities.specs import OpenAPISpec
from logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class ParseOpenAPISpecToEntityCommand(BaseCommand):
    data: dict


@dataclass(frozen=True)
class ParseOpenAPISpecToEntityCommandHandler(
    CommandHandler[ParseOpenAPISpecToEntityCommand, OpenAPISpec]
):
    async def handle(self, command: ParseOpenAPISpecToEntityCommand) -> OpenAPISpec: ...
