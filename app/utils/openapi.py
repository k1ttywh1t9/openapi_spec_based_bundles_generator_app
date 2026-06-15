from typing import Any, Dict


class OpenAPIRefResolver:
    """Helper tool for recursive retrieving by $ref links."""

    def __init__(self, raw_openapi: Dict[str, Any]):
        self._raw_openapi = raw_openapi
        self._components = raw_openapi.get("components", {})
        self._schemas = self._components.get("schemas", {})

    def resolve_schema(self, schema_node: Dict[str, Any]) -> Dict[str, Any]:
        """Рекурсивно заменяет все $ref на реальные тела схем, чтобы изолировать ресурс."""
        if not isinstance(schema_node, dict):
            return schema_node

        # If direct $ref link found
        if "$ref" in schema_node:
            ref_path = schema_node["$ref"]
            # Usually, link looks like that: "#/components/schemas/UserCreate"
            if ref_path.startswith("#/components/schemas/"):
                schema_name = ref_path.split("/")[-1]
                actual_schema = self._schemas.get(schema_name, {})

                # Рекурсивно разрешаем внутренности вытащенной схемы (там тоже могут быть $ref)
                resolved = self.resolve_schema(actual_schema)

                # Опционально: подмешиваем имя схемы в метаданные, чтобы генератор кода знал имя класса
                if isinstance(resolved, dict):
                    return {"__model_name__": schema_name, **resolved}
                return resolved

        # Если это обычный объект со свойствами, бежим вглубь по его полям
        resolved_node = {}
        for key, value in schema_node.items():
            if isinstance(value, dict):
                resolved_node[key] = self.resolve_schema(value)
            elif isinstance(value, list):
                resolved_node[key] = [
                    self.resolve_schema(item) if isinstance(item, dict) else item
                    for item in value
                ]
            else:
                resolved_node[key] = value

        return resolved_node
