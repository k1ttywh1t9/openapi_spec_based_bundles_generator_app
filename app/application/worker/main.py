import asyncio
import logging

from application.worker.adapters.inbound.openapi import OpenAPISpecInboundAdapter
from application.worker.application import WorkerApplication
from logic.init_container import init_container

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


async def main():
    container = init_container()

    container.register(OpenAPISpecInboundAdapter)

    app = WorkerApplication(container=container)
    await app.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
