from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from domain.entities.specs import OpenAPISpec


@patch("domain.entities.specs.NewOpenAPISpecEntityCreatedEvent")
def test_openapi_spec_creation(mock_event_cls):
    mock_event_instance = MagicMock()
    mock_event_cls.return_value = mock_event_instance

    spec_data = {"openapi": "3.0.0", "info": {"title": "Test API"}}
    spec = OpenAPISpec.create_openapi_spec(data=spec_data)

    assert spec.data == spec_data
    mock_event_cls.assert_called_once_with(openapi_spec_oid=spec.oid)
    assert spec._events == [mock_event_instance]
