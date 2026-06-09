from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.entities.specs import OpenAPISpec
from infra.repositories.base import BaseRepository
from infra.repositories.filters.specs import GetOpenAPISpecsFilters


@dataclass
class BaseOpenAPISpecsRepository(
    BaseRepository[OpenAPISpec, GetOpenAPISpecsFilters], ABC
):

    @abstractmethod
    async def check_item_exists_by_title(self, title: str) -> bool: ...
