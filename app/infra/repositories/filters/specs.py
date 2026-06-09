from dataclasses import dataclass

from infra.repositories.filters.base import GetFilters


@dataclass
class GetOpenAPISpecsFilters(GetFilters):
    pass
