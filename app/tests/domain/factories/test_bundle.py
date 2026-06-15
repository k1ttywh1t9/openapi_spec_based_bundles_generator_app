# tests/unit/domain/factories/test_bundle_factory.py
import pytest
from uuid import uuid4
from domain.entities.specs import OpenAPISpec
from domain.factories.resources import APIResourcesBundleFactory  # Твой путь к фабрике
from domain.entities.resources import APIResourcesBundle, APIResource

# Сюда ты можешь дописывать новые конфигурации для проверки парсинга разного говна
# Структура кортежа: (название_теста, сырой_словарь_openapi, ожидаемое_колво_эндпоинтов)
openapi_test_cases = [
    (
        "simple_get_endpoint",
        {
            "paths": {
                "/api/v1/health": {
                    "get": {
                        "summary": "Check health status",
                        "responses": {
                            "200": {
                                "content": {
                                    "application/json": {"schema": {"type": "object"}}
                                }
                            }
                        },
                    }
                }
            }
        },
        1,  # Ждем 1 эндпоинт
    ),
    (
        "post_with_body_and_refs",
        {
            "paths": {
                "/api/v1/items": {
                    "post": {
                        "summary": "Create Item",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/ItemCreate"
                                    }
                                }
                            }
                        },
                        "responses": {
                            "201": {
                                "content": {
                                    "application/json": {"schema": {"type": "object"}}
                                }
                            }
                        },
                    }
                }
            },
            "components": {
                "schemas": {
                    "ItemCreate": {
                        "type": "object",
                        "properties": {"name": {"type": "string"}},
                    }
                }
            },
        },
        1,
    ),
    (
        "ignore_invalid_http_methods",
        {
            "paths": {
                "/api/v1/data": {
                    "options": {
                        "summary": "CORS preflight"
                    },  # Должен проигнорироваться
                    "get": {"summary": "Real data"},  # Должен спарситься
                }
            }
        },
        1,
    ),
]


@pytest.mark.parametrize("name, raw_data, expected_count", openapi_test_cases)
def test_factory_creates_bundle_from_various_specs(name, raw_data, expected_count):
    """Параметризованный тест: проверяет сборку бандла под разной нагрузкой структур."""

    # 1. Arrange: Создаем фейковую сущность спеки, как будто она пришла из Шага 1
    spec = OpenAPISpec(oid=uuid4(), title=f"Test Spec {name}", data=raw_data)

    # 2. Act: Стучимся в фабрику домена
    bundle = APIResourcesBundleFactory.create_from_openapi_spec(spec)

    # 3. Assert: Проверяем целостность агрегата
    assert isinstance(bundle, APIResourcesBundle)
    assert bundle.spec_oid == spec.oid

    # Проверяем, сколько ресурсов зарегистрировалось внутри бандла
    # (замени .resources или метод получения ресурсов на свой актуальный)
    assert len(bundle.resources) == expected_count

    if expected_count > 0:
        first_resource = bundle.resources[0]
        assert isinstance(first_resource, APIResource)
        assert first_resource.method in ["GET", "POST", "PUT", "DELETE", "PATCH"]
        assert first_resource.path.startswith("/")


def test_factory_extracts_full_schemas_and_params():
    """Детальный тест: проверяет, что фабрика вытащила request_schema и параметры."""
    complex_openapi = {
        "paths": {
            "/users/{id}": {
                "get": {
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "integer"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/UserRead"}
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "UserRead": {
                    "type": "object",
                    "properties": {"id": {"type": "integer"}},
                }
            }
        },
    }

    spec = OpenAPISpec(oid=uuid4(), title="Complex Spec", data=complex_openapi)
    bundle = APIResourcesBundleFactory.create_from_openapi_spec(spec)

    resource: APIResource = bundle.resources[0]

    # Проверяем параметры
    assert len(resource.parameters) == 1
    assert resource.parameters[0]["name"] == "id"

    # Проверяем, что схема ответа инлайново развернулась резолвером и привязалась к ресурсу
    assert isinstance(resource.response_schema, dict)
    assert resource.response_schema["__model_name__"] == "UserRead"
    assert resource.response_schema["type"] == "object"
