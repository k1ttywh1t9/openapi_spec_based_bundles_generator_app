from datetime import datetime
from unittest.mock import patch, MagicMock
import pytest

from domain.entities.resources import (
    APIResource,
    ControllerResource,
    ViewResource,
    MVCResource,
    MVCResourcesBundle,
)


def test_api_resource_creation_fields_initialization():
    """Testing correct initialization for fields in APIResource Entity."""
    path = "/api/v1/users/{user_id}/profile"
    method = "GET"
    schema = {"response": "UserSchema"}

    resource = APIResource.create(path=path, method=method, schema=schema)

    assert resource.path == path
    assert resource.method == method
    assert resource.schema == schema


def test_api_resource_title_generation():
    """Testing correct specific business-logic for generation title from path for APIResource Entity."""

    path = "/api/v1/users/{user_id}/profile"
    resource = APIResource.create(path=path, method="GET", schema={})

    assert resource.title == "api_v1_users__user_id__profile"


@patch("domain.entities.resources.NewAPIResourceCreatedEvent")
def test_api_resource_creation_triggers_domain_event(mock_event_cls):
    """Testing correct generation and domain event registration for APIResource Entity."""

    mock_event_instance = MagicMock()
    mock_event_cls.return_value = mock_event_instance

    path = "/api/v1/users/{user_id}/profile"
    resource = APIResource.create(path=path, method="GET", schema={})

    mock_event_cls.assert_called_once_with(
        api_resource_oid=resource.oid,
        api_resource_title="api_v1_users__user_id__profile",
    )
    assert resource._events == [mock_event_instance]
