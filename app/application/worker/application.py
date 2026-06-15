import asyncio
import logging
import signal
from punq import Container

from application.worker.adapters.inbound.openapi import OpenAPISpecInboundAdapter
from infra.message_brokers.base import BaseMessageBroker

logger = logging.getLogger(__name__)


class WorkerApplication:
    def __init__(self, container: Container):
        self._container = container
        self._broker = container.resolve(BaseMessageBroker)
        self._shutdown_event = asyncio.Event()

    async def run(self) -> None:
        logger.info("Initializing Worker Application...")

        self._setup_signal_handlers()

        await self._broker.start()

        openapi_consumer = self._container.resolve(OpenAPISpecInboundAdapter)
        await openapi_consumer.start()

        logger.info("Worker is fully operational and waiting for messages.")

        await self._shutdown_event.wait()

        await self._shutdown()

    def _setup_signal_handlers(self) -> None:
        try:
            loop = asyncio.get_running_loop()
            for sig in (signal.SIGINT, signal.SIGTERM):
                loop.add_signal_handler(sig, self._handle_exit_signal, sig)
        except NotImplementedError:
            pass

    def _handle_exit_signal(self, sig: signal.Signals) -> None:
        logger.info(
            f"Received shutdown signal ({sig.name}). Stopping worker gracefully..."
        )
        self._shutdown_event.set()

    async def _shutdown(self) -> None:
        logger.info("Closing message broker connections...")
        await self._broker.close()
        logger.info("Worker application stopped safely.")
