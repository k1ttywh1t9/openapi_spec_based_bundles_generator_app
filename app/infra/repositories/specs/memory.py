from dataclasses import dataclass, field
from typing import Iterable

from domain.entities.specs import OpenAPISpec
from infra.repositories.filters.specs import GetOpenAPISpecsFilters
from infra.repositories.specs.base import BaseOpenAPISpecsRepository


@dataclass
class MemoryOpenAPISpecRepository(BaseOpenAPISpecsRepository):
    _saved_specs: list[OpenAPISpec] = field(default_factory=list, kw_only=True)

    async def check_spec_exists_by_title(self, title: str) -> bool:
        try:
            return bool(
                next(
                    spec
                    for spec in self._saved_specs
                    if spec.title.as_generic_type() == title
                )
            )
        except StopIteration:
            return False

    async def get_spec_by_oid(self, oid: str) -> OpenAPISpec | None:
        try:
            return next(spec for spec in self._saved_specs if spec.oid == oid)
        except StopIteration:
            return None

    async def add_spec(self, spec: OpenAPISpec) -> None:
        self._saved_specs.append(spec)

    async def get_all_specs(
        self, filters: GetOpenAPISpecsFilters
    ) -> Iterable[OpenAPISpec]:
        specs = self._saved_specs[filters.offset : filters.offset + filters.limit]
        return specs
