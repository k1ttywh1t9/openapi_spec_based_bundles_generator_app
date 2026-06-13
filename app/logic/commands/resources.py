from collections.abc import Iterable
from dataclasses import dataclass

from domain.entities.resources import APIResourcesBundle
from infra.repositories.resources.base import BaseAPIResourcesBundlesRepository
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from logic.commands.base import BaseCommand, CommandHandler
from logic.exceptions.specs import OpenAPINotFoundException


@dataclass(frozen=True)
class CreateAPIResourcesBundleFromSpecCommand(BaseCommand):
    spec_oid: str


@dataclass(frozen=True)
class CreateAPIResourcesBundleFromSpecCommandHandler(
    CommandHandler[CreateAPIResourcesBundleFromSpecCommand, APIResourcesBundle]
):
    specs_repository: BaseOpenAPISpecsRepository
    bundles_repository: BaseAPIResourcesBundlesRepository

    async def handle(
        self, command: CreateAPIResourcesBundleFromSpecCommand
    ) -> APIResourcesBundle:
        spec = await self.specs_repository.get_item_by_oid(command.spec_oid)
        if not spec:
            raise OpenAPINotFoundException(command.spec_oid)

        bundle = APIResourcesBundle.create_from_spec(spec=spec)

        await self.resources_bundle_repository.add_item(bundle)

        await self._mediator.publish(bundle.pull_events())

        return bundle
