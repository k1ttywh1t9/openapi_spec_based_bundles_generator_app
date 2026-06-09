# specs/memory.py
from dataclasses import dataclass
from domain.entities.specs import OpenAPISpec
from infra.repositories.filters.specs import GetOpenAPISpecsFilters
from infra.repositories.memory import BaseMemoryRepository
from infra.repositories.specs.base import BaseOpenAPISpecsRepository


@dataclass
class MemoryOpenAPISpecRepository(
    BaseMemoryRepository[OpenAPISpec, GetOpenAPISpecsFilters],
    BaseOpenAPISpecsRepository,
):

    async def check_item_exists_by_title(self, title: str) -> bool:
        try:
            return bool(
                next(
                    item
                    for item in self._saved_items
                    if getattr(item.title, "value", item.title) == title
                )
            )
        except StopIteration:
            return False
