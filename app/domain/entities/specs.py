from dataclasses import dataclass


from domain.events.specs import NewOpenAPISpecEntityCreatedEvent
from domain.entities.base import BaseEntity
from domain.values.resources import Title


@dataclass(eq=False)
class OpenAPISpec(BaseEntity):
    title: Title
    data: dict

    @classmethod
    def create(cls, title: Title, data: dict):
        new_openapi_spec = cls(title=title, data=data)

        new_openapi_spec.register_event(
            NewOpenAPISpecEntityCreatedEvent(
                spec_title=new_openapi_spec.title.as_generic_type(),
                spec_oid=new_openapi_spec.oid,
            )
        )

        return new_openapi_spec
