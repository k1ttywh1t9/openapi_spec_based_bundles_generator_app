from dataclasses import dataclass

from domain.entities.specs import OpenAPISpec
from domain.values.resources import Title
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from logic.commands.base import BaseCommand, CommandHandler
from logic.exceptions.specs import OpenAPISpecWithThatTitleAlreadyExistsException


@dataclass(frozen=True)
class CreateNewOpenAPISpecEntityFromRawCommand(BaseCommand):
    title: str
    data: dict


@dataclass(frozen=True)
class CreateNewOpenAPISpecEntityFromRawCommandHandler(
    CommandHandler[CreateNewOpenAPISpecEntityFromRawCommand, OpenAPISpec]
):
    specs_repository: BaseOpenAPISpecsRepository

    async def handle(
        self, command: CreateNewOpenAPISpecEntityFromRawCommand
    ) -> OpenAPISpec:
        if await self.specs_repository.check_item_exists_by_title(command.title):
            raise OpenAPISpecWithThatTitleAlreadyExistsException(command.title)

        title = Title(value=command.title)

        new_openapi_spec = OpenAPISpec.create(title=title, data=command.data)

        await self.specs_repository.add_item(new_openapi_spec)

        events = new_openapi_spec.pull_events()

        await self._mediator.publish(events=events)

        return new_openapi_spec
