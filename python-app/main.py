import os
import json
import asyncio
import httpx
from agent.chains import chain
from utils.chunking import get_schema_chunks, get_short_name
from core.config import settings

import logging


from pathlib import Path

# Вместо нескольких блоков, используйте один чистый блок:
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

# Создаем конкретные логгеры
logger = logging.getLogger("generator")
# Уровень DEBUG для детального отслеживания
logger.setLevel(logging.DEBUG)

# Включаем логирование HTTP-запросов (Ollama)
logging.getLogger("httpx").setLevel(logging.DEBUG)


semaphore = asyncio.Semaphore(3)


async def load_openapi_spec():
    if settings.openapi.url:
        print(f"🌐 Загрузка спецификации из: {settings.openapi.url}")
        async with httpx.AsyncClient() as client:
            response = await client.get(settings.openapi.url)
            response.raise_for_status()
            return response.json()
    elif settings.openapi.path:
        print(f"📁 Чтение файла: {settings.openapi.path}")
        with open(settings.openapi.path, "r", encoding="utf-8") as f:
            return json.load(f)
    raise ValueError("Укажите openapi.path или openapi.url!")


def save_artifacts(entity_name, artifacts):
    # СОКРАЩАЕМ ИМЯ ТУТ
    short_entity_name = get_short_name(entity_name)
    base_dir = Path("generated_code") / short_entity_name.lower()

    for art in artifacts:
        # Формируем полный путь
        # art.filename может быть 'schemas/model.py' или 'routes.py'
        file_path = base_dir / art.filename

        # Создаем все нужные подпапки (например, schemas/) автоматически
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Записываем код
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(art.code)
        print(f"✅ Создан файл: {file_path}")


# main.py
async def run_generation():
    data = await load_openapi_spec()
    tasks = []

    for model_name, schema, paths in get_schema_chunks(data):
        tasks.append(process_entity(model_name, schema, paths))

    await asyncio.gather(*tasks)


async def process_entity(model_name, schema, paths):
    # ПРОВЕРКА: Если папка сущности уже существует, пропускаем
    output_dir = os.path.join("generated_code", model_name.lower())
    if os.path.exists(output_dir):
        # Проверяем, не пустая ли она (можно убрать проверку на файлы, если достаточно папки)
        if os.listdir(output_dir):
            print(f"⏩ Пропускаем {model_name} (уже существует)")
            return

    try:
        async with semaphore:
            print(f"🚀 Генерация для: {model_name}...")
            chunk_data = {"schema": schema, "paths": paths}
            result = await chain.ainvoke(
                {"entity_name": model_name, "openapi_chunk": json.dumps(chunk_data)}
            )
            save_artifacts(model_name, result.artifacts)
    except Exception as e:
        print(f"❌ Ошибка генерации для {model_name}: {e}")


if __name__ == "__main__":
    asyncio.run(run_generation())
