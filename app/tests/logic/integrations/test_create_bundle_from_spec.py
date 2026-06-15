import pytest
from punq import Container

from domain.entities.specs import OpenAPISpec
from infra.message_brokers.base import BaseMessageBroker
from infra.repositories.resources.base import BaseAPIResourcesBundlesRepository
from application.worker.adapters.inbound.openapi import OpenAPISpecInboundAdapter
from settings.main import Settings


@pytest.mark.asyncio
async def test_create_bundle_from_spec_success(
    parsed_spec: OpenAPISpec, container: Container
):
    # Arrange
    message_broker = container.resolve(BaseMessageBroker)
    repository = container.resolve(BaseAPIResourcesBundlesRepository)
    settings = container.resolve(Settings)

    topic = settings.message_broker.topics.new_openapi_spec_entity_created_topic

    assert len(message_broker._topics[topic]) == 1, "Step 1 event has to be in broker"

    raw_message_bytes = message_broker._topics[topic][0]

    container.register(OpenAPISpecInboundAdapter)
    worker_adapter = container.resolve(OpenAPISpecInboundAdapter)

    await worker_adapter.process_message(raw_message_bytes)

    all_bundles = list(await repository.get_all_items())
    assert (
        len(all_bundles) == 1
    ), "API Resources bundle has to be created automatically via core handler after trigger from worker"

    saved_bundle = all_bundles[0]
    assert saved_bundle.spec_oid == parsed_spec.oid
