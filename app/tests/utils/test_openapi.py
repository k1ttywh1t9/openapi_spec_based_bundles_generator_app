# tests/unit/utils/test_openapi_resolver.py
import pytest
from utils.openapi import (
    OpenAPIRefResolver,
)


@pytest.fixture
def sample_openapi_data():
    return {
        "openapi": "3.1.0",
        "components": {
            "schemas": {
                "UserRole": {"type": "string", "enum": ["admin", "user"]},
                "UserCreate": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string", "format": "email"},
                        "role": {
                            "$ref": "#/components/schemas/UserRole"
                        },  # Nested reference
                    },
                    "required": ["email"],
                },
            }
        },
    }


def test_resolver_resolves_nested_references(sample_openapi_data):
    """Проверяем, что резолвер полностью разворачивает граф `$ref` вглубь."""
    resolver = OpenAPIRefResolver(raw_openapi=sample_openapi_data)

    # Take schema that contains link to other schema
    target_node = {"$ref": "#/components/schemas/UserCreate"}

    resolved_schema = resolver.resolve_schema(target_node)

    # Testing that high level has been unnested
    assert resolved_schema["__model_name__"] == "UserCreate"
    assert resolved_schema["type"] == "object"
    assert "email" in resolved_schema["properties"]

    # Testing that nested link "role" was unnested too
    nested_role = resolved_schema["properties"]["role"]
    assert isinstance(nested_role, dict)
    assert nested_role["__model_name__"] == "UserRole"
    assert nested_role["type"] == "string"
    assert "admin" in nested_role["enum"]


def test_resolver_handles_missing_refs():
    """Проверяем, что резолвер не падает, если в спеке битая ссылка."""
    broken_openapi = {"components": {"schemas": {}}}
    resolver = OpenAPIRefResolver(raw_openapi=broken_openapi)

    node = {"$ref": "#/components/schemas/NonExistent"}
    resolved = resolver.resolve_schema(node)

    # If ref corrupted, empty dict has to be returned, or source node (based on realization)

    assert isinstance(resolved, dict)
