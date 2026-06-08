from datetime import datetime
from unittest.mock import MagicMock

from domain.entities.base import BaseEntity


def test_base_entity_initialization():
    class TestEntity(BaseEntity):
        pass

    entity1 = TestEntity()
    entity2 = TestEntity()

    assert entity1.oid is not None
    assert isinstance(entity1.oid, str)
    assert entity1.oid != entity2.oid
    assert isinstance(entity1.created_at, datetime)
    assert entity1._events == []


def test_base_entity_equality_and_hash():
    class TestEntity(BaseEntity):
        pass

    entity1 = TestEntity(oid="same-id")
    entity2 = TestEntity(oid="same-id")
    entity3 = TestEntity(oid="different-id")

    # Сравнение идет по oid
    assert entity1 == entity2
    assert entity1 != entity3
    assert hash(entity1) == hash(entity2)
    assert hash(entity1) != hash(entity3)


def test_base_entity_event_lifecycle():
    class TestEntity(BaseEntity):
        pass

    entity = TestEntity()
    mock_event_1 = MagicMock()
    mock_event_2 = MagicMock()

    assert len(entity._events) == 0

    entity.register_event(mock_event_1)
    entity.register_event(mock_event_2)
    assert len(entity._events) == 2

    events = entity.pull_events()
    assert len(events) == 2
    assert mock_event_1 in events
    assert mock_event_2 in events

    assert len(entity._events) == 0
