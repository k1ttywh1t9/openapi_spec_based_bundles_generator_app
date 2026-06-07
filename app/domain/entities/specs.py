from dataclasses import dataclass
import json

from settings.config import Settings
from domain.entities.base import BaseEntity


@dataclass
class OpenAPISpec(BaseEntity):
    data: dict

    @classmethod
    def create_openapi_spec(cls, data: dict):
        new_openapi_spec = cls(data=data)
        return new_openapi_spec
