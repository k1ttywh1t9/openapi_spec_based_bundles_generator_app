from dataclasses import dataclass
import json

from domain.values.resources import HTMLTemplate
from settings.config import Settings
from domain.entities.base import BaseEntity


@dataclass(eq=False)
class APIResource(BaseEntity):
    path: str
    method: str
    schema: dict

    @classmethod
    def create_api_resource(cls, path: str, method: str, schema: dict):
        new_resource = cls(path=path, method=method, schema=schema)
        return new_resource


@dataclass(eq=False)
class UIResource(BaseEntity):
    api_resource: APIResource

    template: HTMLTemplate
    handlers: str
    schema: dict

    @classmethod
    def create_ui_resource(
        cls, api_resource: APIResource, template: str, handlers: str, schema: dict
    ):
        new_resource = cls(
            api_resource=api_resource,
            template=template,
            handlers=handlers,
            schema=schema,
        )
        return new_resource
