from dataclasses import dataclass

from domain.entities.resources import APIResource, APIResourcesBundle
from domain.entities.specs import OpenAPISpec
from utils.openapi import OpenAPIRefResolver


@dataclass
class APIResourcesBundleFactory:
    @staticmethod
    def create_from_openapi_spec(spec: OpenAPISpec) -> APIResourcesBundle:
        """
        Factory method for collecting APIResourceBundle
        with full graphs of schemas and parameters from OpenAPISpec.
        """
        bundle = APIResourcesBundle(spec_oid=spec.oid)
        raw_openapi = spec.data
        paths = raw_openapi.get("paths", {})

        # Инициализируем наш резолвер контекстом текущей спецификации
        resolver = OpenAPIRefResolver(raw_openapi=raw_openapi)

        for path_url, path_item in paths.items():
            for method, operation_data in path_item.items():
                if method.lower() not in ["get", "post", "put", "delete", "patch"]:
                    continue

                resource_title = (
                    operation_data.get("summary") or f"{method.upper()} {path_url}"
                )

                # --- ВЫТАСКИВАЕМ МЯСО РЕСУРСА ---

                # 1. Вытаскиваем параметры запроса (Query, Path, Headers)
                raw_parameters = operation_data.get("parameters", [])
                # Разрешаем рефки в параметрах, если они есть
                resolved_parameters = [
                    resolver.resolve_schema(p) for p in raw_parameters
                ]

                # 2. Вытаскиваем тело запроса (Request Body)
                resolved_request_schema = {}
                request_body = operation_data.get("requestBody", {})
                if request_body:
                    # Разрешаем рефку самого requestBody, если она есть
                    request_body = resolver.resolve_schema(request_body)
                    # Вытаскиваем схему контента (обычно application/json)
                    content = request_body.get("content", {})
                    json_content = content.get("application/json", {})
                    if "schema" in json_content:
                        resolved_request_schema = resolver.resolve_schema(
                            json_content["schema"]
                        )

                # 3. Вытаскиваем успешный ответ (Response 200/201)
                resolved_response_schema = {}
                responses = operation_data.get("responses", {})
                # Берем первый успешный статус из того что есть
                success_status = next(
                    (status for status in ["200", "201", "204"] if status in responses),
                    None,
                )
                if success_status:
                    response_data = resolver.resolve_schema(responses[success_status])
                    content = response_data.get("content", {})
                    json_content = content.get("application/json", {})
                    if "schema" in json_content:
                        resolved_response_schema = resolver.resolve_schema(
                            json_content["schema"]
                        )

                # 4. Собираем полноценную доменную сущность ресурса
                resource = APIResource(
                    title=resource_title,
                    path=path_url,
                    method=method.upper(),
                    parameters=resolved_parameters,  # Передаем полный разрешенный список
                    request_schema=resolved_request_schema,  # Передаем полностью развернутый JSON структуры
                    response_schema=resolved_response_schema,  # Передаем полностью развернутый JSON ответа
                )

                bundle.add_resource(resource)

        return bundle
