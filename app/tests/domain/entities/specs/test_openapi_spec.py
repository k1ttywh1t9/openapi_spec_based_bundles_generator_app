# app/tests/domain/entities/specs/test_openapi_spec.py
from unittest.mock import MagicMock, patch
import pytest

from domain.entities.specs import OpenAPISpec
from domain.values.resources import Title


@pytest.fixture
def dummy_spec_setup():
    title = Title("test_openapi_spec")
    data = {"openapi": "3.0.0", "info": {"title": "Test API"}}
    return title, data


def test_openapi_spec_fields_initialization_success(dummy_spec_setup):
    spec_title, spec_data = dummy_spec_setup

    spec = OpenAPISpec.create(title=spec_title, data=spec_data)

    assert spec.data == spec_data
    assert spec.title == spec_title
    assert spec.oid is not None, "New entity have auto-generated UUID"


@patch("domain.entities.specs.NewOpenAPISpecEntityCreatedEvent")
def test_openapi_spec_creation_triggers_correct_domain_event_success(
    mock_event_cls, dummy_spec_setup
):
    spec_title, spec_data = dummy_spec_setup
    mock_event_instance = MagicMock()
    mock_event_cls.return_value = mock_event_instance

    spec = OpenAPISpec.create(title=spec_title, data=spec_data)

    mock_event_cls.assert_called_once_with(
        spec_title=spec.title.as_generic_type(),
        spec_oid=spec.oid,
    )


@patch("domain.entities.specs.NewOpenAPISpecEntityCreatedEvent")
def test_openapi_spec_registers_event_in_internal_lifecycle_success(
    mock_event_cls, dummy_spec_setup
):
    spec_title, spec_data = dummy_spec_setup
    mock_event_instance = MagicMock()
    mock_event_cls.return_value = mock_event_instance

    spec = OpenAPISpec.create(title=spec_title, data=spec_data)

    assert mock_event_instance in spec._events
    assert len(spec._events) == 1
