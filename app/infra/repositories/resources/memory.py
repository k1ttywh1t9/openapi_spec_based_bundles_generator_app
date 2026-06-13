# app/infra/repositories/resources/memory.py
from dataclasses import dataclass

from domain.entities.resources import APIResource, APIResourcesBundle
from infra.repositories.filters.resources import (
    GetAPIResourcesBundleFilters,
    GetAPIResourcesFilters,
)
from infra.repositories.memory import MemoryRepository
from infra.repositories.resources.base import (
    BaseAPIResourcesBundlesRepository,
    BaseAPIResourcesRepository,
)


@dataclass
class MemoryAPIResourcesRepository(
    MemoryRepository[APIResource, GetAPIResourcesFilters],
    BaseAPIResourcesRepository,
):
    pass


@dataclass
class MemoryAPIResourcesBundleRepository(
    MemoryRepository[APIResourcesBundle, GetAPIResourcesBundleFilters],
    BaseAPIResourcesBundlesRepository,
):
    pass
