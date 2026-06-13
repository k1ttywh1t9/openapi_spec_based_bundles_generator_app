import asyncio
import logging
import signal

from infra.message_brokers.base import BaseMessageBroker
from logic.events.integrations.specs import OpenAPISpecEntityReceivedFromBrokerEvent
from logic.init_container import init_container
from logic.mediator.main import Mediator

import orjson

from settings.main import Settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

keep_running = True


async def run_worker(settings: Settings, broker: BaseMessageBroker, mediator: Mediator):
    """Register message processing callback."""

    async def process_message(body: bytes):
        try:
            logger.info("Received message from broker, unpacking...")
            data = orjson.loads(body)

            broker_event = OpenAPISpecEntityReceivedFromBrokerEvent(
                spec_oid=data["spec_oid"]
            )

            await mediator.publish([broker_event])
            logger.info(f"Successfully processed spec with OID: {data['spec_oid']}")

        except Exception as e:
            logger.error(f"Error while processing broker message: {e}", exc_info=True)
            # In concrete broker realization the nack (negative ack) logic will be here, but
            # with MemoryMessageBroker we just logging.

    topic = settings.message_broker.topics.new_openapi_spec_entity_created_topic
    await broker.start_consuming(
        topic=topic,
        callback=process_message,
    )
    logger.info("Worker subscribed to topic: " + topic)


async def main():
    global keep_running
    logger.info("Starting Async Worker Application...")

    container = init_container()

    broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    mediator: Mediator = container.resolve(Mediator)
    settings: Settings = container.resolve(Settings)

    loop = asyncio.get_running_loop()

    def shutdown_handler():
        global keep_running
        logger.info("Received shutdown signal. Stopping worker...")
        keep_running = False

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, shutdown_handler)

    await broker.start()
    await run_worker(settings=settings, broker=broker, mediator=mediator)

    logger.info("Worker is fully operational and waiting for messages.")

    while keep_running:
        await asyncio.sleep(1)

    logger.info("Closing message broker connections...")
    await broker.close()
    logger.info("Worker application stopped safely.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
