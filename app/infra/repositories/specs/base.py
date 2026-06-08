from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass

from domain.entities.specs import OpenAPISpec
from infra.repositories.filters.specs import GetOpenAPISpecsFilters


@dataclass
class BaseOpenAPISpecsRepository(ABC):
    @abstractmethod
    async def check_spec_exists_by_title(self, title: str) -> bool: ...

    @abstractmethod
    async def get_spec_by_oid(self, oid: str) -> OpenAPISpec | None: ...

    @abstractmethod
    async def add_spec(self, spec: OpenAPISpec) -> None: ...

    @abstractmethod
    async def get_all_specs(
        self, filters: GetOpenAPISpecsFilters
    ) -> Iterable[OpenAPISpec]: ...
