# application/cli/upload_spec.py
import asyncio
import logging
import argparse
from pathlib import Path
import orjson

from logic.init_container import init_container
from logic.mediator.main import Mediator
from logic.commands.specs import CreateNewOpenAPISpecEntityFromRawCommand
from infra.message_brokers.base import BaseMessageBroker

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


async def upload_spec_via_cli(file_path: str, title: str):
    path = Path(file_path)
    if not path.exists():
        logger.error(f"Файл не найден по пути: {file_path}")
        return

    try:
        with open(path, "rb") as f:
            raw_data = orjson.loads(f.read())
    except Exception as e:
        logger.error(f"Ошибка чтения или парсинга JSON: {e}")
        return

    container = init_container()
    mediator = container.resolve(Mediator)
    broker = container.resolve(BaseMessageBroker)

    await broker.start()

    logger.info(f"Загружаем спецификацию '{title}' из файла {file_path}...")

    command = CreateNewOpenAPISpecEntityFromRawCommand(title=title, data=raw_data)

    results = await mediator.handle_command(command)
    created_spec = list(results)[0]

    logger.info(
        f"Шаг 1 успешно завершен через CLI! Спека создана с OID: {created_spec.oid}"
    )

    await broker.close()


def main():
    parser = argparse.ArgumentParser(
        description="CLI инструмент для загрузки OpenAPI спецификаций в систему."
    )
    parser.add_argument(
        "--file", "-f", required=True, type=str, help="Путь к файлу openapi.json"
    )
    parser.add_argument(
        "--title",
        "-t",
        default="CLI Uploaded API",
        type=str,
        help="Название спецификации",
    )

    args = parser.parse_args()

    asyncio.run(upload_spec_via_cli(file_path=args.file, title=args.title))


if __name__ == "__main__":
    main()
