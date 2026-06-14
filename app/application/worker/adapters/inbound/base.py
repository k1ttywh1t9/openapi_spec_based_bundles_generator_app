import logging
from abc import ABC, abstractmethod
from infra.message_brokers.base import BaseMessageBroker

logger = logging.getLogger(__name__)


class BaseInboundAdapter(ABC):
    """Базовый класс для всех потребителей сообщений из брокера."""

    def __init__(self, broker: BaseMessageBroker):
        self._broker = broker

    @property
    @abstractmethod
    def topic(self) -> str:
        """Топик брокера, на который подписывается консьюмер."""
        pass

    @abstractmethod
    async def process_message(self, body: bytes) -> None:
        """Специфичная для каждого топика бизнес-логика обработки сообщения."""
        pass

    async def start(self) -> None:
        """Регистрирует безопасный коллбэк для чтения из топика."""

        async def _safe_callback(body: bytes):
            try:
                await self.process_message(body)
            except Exception as e:
                logger.error(
                    f"Unhandled error in consumer {self.__class__.__name__} "
                    f"while processing message from topic '{self.topic}': {e}",
                    exc_info=True,
                )
                # Если появится реальный брокер (Rabbit/Kafka),
                # логика nack() / reject() вызывается здесь

        await self._broker.start_consuming(
            topic=self.topic,
            callback=_safe_callback,
        )
        logger.info(
            f"Consumer {self.__class__.__name__} successfully subscribed to: {self.topic}"
        )
