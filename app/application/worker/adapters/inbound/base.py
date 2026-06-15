from abc import ABC, abstractmethod
import logging

from infra.message_brokers.base import BaseMessageBroker


logger = logging.getLogger(__name__)


class BaseInboundAdapter(ABC):
    def __init__(self, broker: BaseMessageBroker):
        self._broker = broker

    @property
    @abstractmethod
    def topic(self) -> str:
        pass

    @abstractmethod
    async def process_message(self, body: bytes) -> None:
        pass

    async def start(self) -> None:
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
