# utils/chunking.py
import json

import hashlib


def get_short_name(name: str) -> str:
    # Если имя длиннее 20 символов, берем первые 10 и добавляем хэш
    if len(name) > 20:
        hash_part = hashlib.md5(name.encode()).hexdigest()[:6]
        return f"{name[:15]}_{hash_part}"
    return name


def get_schema_chunks(data):
    schemas = data.get("components", {}).get("schemas", {})
    paths = data.get("paths", {})

    for model_name, schema in schemas.items():
        # Берем только пути, содержащие имя модели (базовая логика)
        related_paths = {
            p: v for p, v in paths.items() if model_name.lower() in p.lower()
        }

        # Важно: отдаем структурированные данные
        yield model_name, json.dumps(schema, indent=2), json.dumps(
            related_paths, indent=2
        )
