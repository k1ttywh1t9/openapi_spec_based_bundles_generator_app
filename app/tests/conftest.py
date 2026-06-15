from collections import defaultdict
import pytest
from punq import Container

from infra.message_brokers.base import BaseMessageBroker
from infra.repositories.specs.base import BaseOpenAPISpecsRepository
from logic.init_container import init_container


@pytest.fixture(scope="function")
def container(monkeypatch) -> Container:
    """Чистый инструмент pytest.

    Получает контейнер и изолирует хранилища брокера и репозитория
    для текущего теста, используя monkeypatch.
    """
    # 1. Берем обычный контейнер, который возвращает init_container
    test_container = init_container()

    # 2. Вытаскиваем инстансы инфраструктуры
    message_broker = test_container.resolve(BaseMessageBroker)
    repository = test_container.resolve(BaseOpenAPISpecsRepository)

    # 3. Инструментом monkeypatch подменяем их внутренние словари на абсолютно СВЕЖИЕ.
    # Таким образом, у каждого теста будет свой чистый пустой словарь,
    # который автоматически сотрется после завершения теста.
    if hasattr(message_broker, "_topics"):
        monkeypatch.setattr(message_broker, "_topics", defaultdict(list))

    if hasattr(
        repository, "_saved_items"
    ):  # поменяй на имя словаря внутри InMemoryOpenAPISpecsRepository, если оно другое
        monkeypatch.setattr(repository, "_saved_items", [])

    return test_container
