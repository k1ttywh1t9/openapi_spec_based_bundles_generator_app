from dataclasses import dataclass


from domain.events.specs import NewOpenAPISpecEntityCreatedEvent
from domain.entities.base import BaseEntity


@dataclass(eq=False)
class OpenAPISpec(BaseEntity):
    data: dict

    @classmethod
    def create_openapi_spec(cls, data: dict):
        new_openapi_spec = cls(data=data)

        new_openapi_spec.register_event(
            NewOpenAPISpecEntityCreatedEvent(
                openapi_spec_oid=new_openapi_spec.oid,
            )
        )

        return new_openapi_spec
