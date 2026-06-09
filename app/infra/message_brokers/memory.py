from dataclasses import dataclass, field
from collections import defaultdict
from typing import Callable, Awaitable
import logging

from infra.message_brokers.base import BaseMessageBroker

logger = logging.getLogger(__name__)


@dataclass
class MemoryMessageBroker(BaseMessageBroker):
    _topics: dict[str, list[bytes]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    _subscribers: dict[str, list[Callable[[bytes], Awaitable[None]]]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    _is_running: bool = field(default=False, kw_only=True)

    async def start(self) -> None:
        self._is_running = True
        logger.info("In-Memory message broker started.")

    async def close(self) -> None:
        self._is_running = False
        self._topics.clear()
        self._subscribers.clear()
        logger.info("In-Memory message broker stopped and cleared.")

    async def send_message(self, key: str, topic: str, value: bytes) -> None:
        if not self._is_running:
            raise RuntimeError("Broker is not running. Call .start() first.")

        self._topics[topic].append(value)
        logger.debug(f"Message sent to topic '{topic}' with key '{key}'")

        if topic in self._subscribers and self._subscribers[topic]:
            for subscriber in self._subscribers[topic]:
                await subscriber(value)

    async def start_consuming(
        self, topic: str, callback: Callable[[bytes], Awaitable[None]] = None
    ) -> None:
        """
        Registers a subscriber to a topic.
        Note: In base interface, the `start_consuming` method may not have a `callback` argument
        (depending on how the workers are tied to the broker).
        If workers invoke it differently, adapt the signature.
        """

        if callback:
            self._subscribers[topic].append(callback)
            logger.info(f"Registered consumer for topic '{topic}'")

    async def stop_consuming(self, topic: str) -> None:
        if topic in self._subscribers:
            self._subscribers[topic].clear()
            logger.info(f"Stopped consuming from topic '{topic}'")

    def get_messages(self, topic: str) -> list[bytes]:
        """Allows tests to read everything that hit the topic and validate it."""

        return self._topics[topic]
