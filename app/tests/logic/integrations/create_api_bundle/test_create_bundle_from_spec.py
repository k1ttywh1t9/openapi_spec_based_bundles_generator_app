import pytest
from application.worker.main import run_worker
from infra.message_brokers.base import BaseMessageBroker
from infra.repositories.resources.base import BaseAPIResourcesBundlesRepository
from logic.mediator.main import Mediator


@pytest.mark.asyncio
async def test_step_2_create_bundle_from_spec_success(parsed_spec, container):
    message_broker = container.resolve(BaseMessageBroker)
    mediator = container.resolve(Mediator)
    bundle_repo = container.resolve(BaseAPIResourcesBundlesRepository)

    await run_worker(broker=message_broker, mediator=mediator)

    all_bundles = list(await bundle_repo.get_all_items())
    assert (
        len(all_bundles) == 1
    ), "Бандл ресурсов должен автоматически создаться воркером"

    saved_bundle = all_bundles[0]
    assert saved_bundle.spec_oid == parsed_spec.oids
