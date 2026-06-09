# app/infra/repositories/filters/pipeline.py
from dataclasses import dataclass

from infra.repositories.filters.base import GetFilters


@dataclass
class GetOpenAPISpecsFilters(GetFilters):
    pass


@dataclass
class GetAPIResourcesFilters(GetFilters):
    pass


@dataclass
class GetAPIResourcesBundleFilters(GetFilters):
    pass


@dataclass
class GetControllerResourcesFilters(GetFilters):
    pass


@dataclass
class GetViewResourcesFilters(GetFilters):
    pass


@dataclass
class GetMVCResourcesFilters(GetFilters):
    pass


@dataclass
class GetMVCResourcesBundleFilters(GetFilters):
    pass
