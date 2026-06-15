import logging

import orjson

from application.worker.adapters.inbound.base import BaseInboundAdapter
from infra.message_brokers.base import BaseMessageBroker
from logic.events.integrations.specs import OpenAPISpecEntityReceivedFromBrokerEvent
from logic.mediator.main import Mediator
from settings.main import Settings

logger = logging.getLogger(__name__)


class OpenAPISpecInboundAdapter(BaseInboundAdapter):
    def __init__(
        self, broker: BaseMessageBroker, mediator: Mediator, settings: Settings
    ):
        super().__init__(broker=broker)
        self._mediator = mediator
        self._settings = settings

    @property
    def topic(self) -> str:
        return (
            self._settings.message_broker.topics.new_openapi_spec_entity_created_topic
        )

    async def process_message(self, body: bytes) -> None:
        logger.info("Received message from broker, unpacking...")
        data = orjson.loads(body)

        broker_event = OpenAPISpecEntityReceivedFromBrokerEvent(
            spec_oid=data["spec_oid"]
        )

        await self._mediator.publish([broker_event])
        logger.info(
            f"Successfully dispatched event to Mediator for spec OID: {data['spec_oid']}"
        )
