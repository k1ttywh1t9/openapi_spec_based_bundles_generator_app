from abc import ABC
from dataclasses import dataclass, field
import re

from domain.events.resources import (
    NewAPIResourceCreatedEvent,
    NewControllerResourceCreatedEvent,
    NewMVCResourceCreatedEvent,
    NewMVCResourcesBundleCreatedEvent,
    NewViewResourceCreatedEvent,
)
from domain.values.resources import Title
from domain.values.resources import CodeContent
from domain.entities.base import BaseEntity


@dataclass(eq=False)
class APIResource(BaseEntity):
    path: str
    method: str
    schema: dict

    @property
    def title(self) -> str:
        title = re.sub(r"[^a-zA-Z0-9]", "_", self.path).strip("_")
        return title

    @classmethod
    def create(cls, path: str, method: str, schema: dict):
        new_resource = cls(path=path, method=method, schema=schema)

        new_resource.register_event(
            NewAPIResourceCreatedEvent(
                api_resource_oid=new_resource.oid,
                api_resource_title=new_resource.title,
            )
        )

        return new_resource


@dataclass(eq=False)
class ControllerResource(BaseEntity):
    handlers: CodeContent

    @classmethod
    def create(cls, handlers: str, lang: str) -> "ControllerResource":
        code_vo = CodeContent.from_raw(body=handlers, lang=lang)

        new_resource = cls(handlers=code_vo)
        new_resource.register_event(
            NewControllerResourceCreatedEvent(
                controller_resource_oid=new_resource.oid,
            )
        )
        return new_resource


@dataclass(eq=False)
class ViewResource(BaseEntity):
    template: CodeContent

    @classmethod
    def create(cls, template: str):
        new_resource = cls(template=template)

        new_resource.register_event(
            NewViewResourceCreatedEvent(
                view_resource_oid=new_resource.oid,
            )
        )

        return new_resource


@dataclass(eq=False)
class MVCResource(BaseEntity):
    model_resource: APIResource
    controller_resource: ControllerResource
    view_resource: ViewResource

    @property
    def title(self) -> str:
        title = re.sub(r"[^a-zA-Z0-9]", "_", self.path).strip("_")
        return title

    @classmethod
    def create(cls, template: str):
        new_resource = cls(template=template)

        new_resource.register_event(
            NewMVCResourceCreatedEvent(
                mvc_resource_oid=new_resource.oid,
                mvc_resource_title=new_resource.title,
            )
        )

        return new_resource


@dataclass(eq=False)
class MVCResourcesBundle(BaseEntity):
    title: Title
    resources: set[MVCResource] = field(
        default_factory=set,
        kw_only=True,
    )

    @classmethod
    def create_bundle(cls, title: Title) -> "MVCResourcesBundle":
        new_bundle = cls(title=title)
        new_bundle.register_event(
            NewMVCResourcesBundleCreatedEvent(
                bundle_oid=new_bundle.oid,
                bundle_title=new_bundle.title.as_generic_type(),
            ),
        )
        return new_bundle


#     def add_resource(self, resource: MVCResource):
#         self.messages.add(resource)
#         self.register_event(
#             NewResourceCreatedEvent(
# ...wtf
#             ),
#         )
