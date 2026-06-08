from dataclasses import dataclass


@dataclass
class GetOpenAPISpecsFilters:
    limit: int = 10
    offset: int = 0
