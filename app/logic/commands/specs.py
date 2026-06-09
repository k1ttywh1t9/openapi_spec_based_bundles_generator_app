from dataclasses import dataclass

from domain.entities.specs import OpenAPISpec
from domain.values.resources import Title
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from logic.commands.base import BaseCommand, CommandHandler
from logic.exceptions.specs import OpenAPISpecWithThatTitleAlreadyExistsException


@dataclass(frozen=True)
class ParseOpenAPISpecToEntityCommand(BaseCommand):
    title: str
    data: dict


@dataclass(frozen=True)
class ParseOpenAPISpecToEntityCommandHandler(
    CommandHandler[ParseOpenAPISpecToEntityCommand, OpenAPISpec]
):
    specs_repository: BaseOpenAPISpecsRepository

    async def handle(self, command: ParseOpenAPISpecToEntityCommand) -> OpenAPISpec:
        if await self.specs_repository.check_spec_exists_by_title(command.title):
            raise OpenAPISpecWithThatTitleAlreadyExistsException(command.title)

        title = Title(value=command.title)

        new_openapi_spec = OpenAPISpec.create(title=title)
        # TODO: считать ивенты
        await self.specs_repository.add_spec(new_openapi_spec)
        await self._mediator.publish(new_openapi_spec.pull_events())

        return new_openapi_spec                                                    
