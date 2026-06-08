from unittest.mock import MagicMock, patch

from domain.entities.resources import MVCResourcesBundle, ViewResource


@patch("domain.entities.resources.NewViewResourceCreatedEvent")
def test_view_resource_creation(mock_event_cls):
    mock_event_instance = MagicMock()
    mock_event_cls.return_value = mock_event_instance

    template_code = "<h1>Hello</h1>"
    resource = ViewResource.create(template=template_code)

    assert resource.template == template_code
    mock_event_cls.assert_called_once_with(view_resource_oid=resource.oid)
    assert resource._events == [mock_event_instance]


@patch("domain.entities.resources.NewMVCResourcesBundleCreatedEvent")
def test_mvc_resources_bundle_creation(mock_event_cls):
    mock_event_instance = MagicMock()
    mock_event_cls.return_value = mock_event_instance

    # Эмулируем доменный Value Object Title
    mock_title = MagicMock()
    mock_title.as_generic_type.return_value = "Generic Bundle Title"

    bundle = MVCResourcesBundle.create_bundle(title=mock_title)

    assert bundle.title == mock_title
    assert isinstance(bundle.resources, set)
    assert len(bundle.resources) == 0

    mock_event_cls.assert_called_once_with(
        bundle_oid=bundle.oid, bundle_title="Generic Bundle Title"
    )
    assert bundle._events == [mock_event_instance]
