# app/infra/repositories/resources/base.py
from abc import ABC
from dataclasses import dataclass

from domain.entities.resources import APIResource, APIResourcesBundle
from infra.repositories.base import BaseRepository
from infra.repositories.filters.resources import (
    GetAPIResourcesBundleFilters,
    GetAPIResourcesFilters,
)


@dataclass
class BaseAPIResourcesRepository(
    BaseRepository[APIResource, GetAPIResourcesFilters], ABC
):
    pass


@dataclass
class BaseAPIResourcesBundleRepository(
    BaseRepository[APIResourcesBundle, GetAPIResourcesBundleFilters], ABC
):
    pass
