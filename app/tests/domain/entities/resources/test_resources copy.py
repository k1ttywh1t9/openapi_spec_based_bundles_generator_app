# from unittest.mock import patch, MagicMock
# import pytest

# from domain.entities.resources import (
#     APIResource,
#     ControllerResource,
#     ViewResource,
#     MVCResourcesBundle,
# )

# # =====================================================================
# # APIResource Tests
# # =====================================================================


# def test_api_resource_fields_initialization():
#     """Проверяем только корректную инициализацию полей сущности APIResource."""
#     path = "/api/v1/users/{user_id}/profile"
#     method = "GET"
#     schema = {"response": "UserSchema"}

#     resource = APIResource.create(path=path, method=method, schema=schema)

#     assert resource.path == path
#     assert resource.method == method
#     assert resource.schema == schema


# def test_api_resource_title_generation():
#     """Проверяем специфичную бизнес-логику генерации title из пути."""
#     path = "/api/v1/users/{user_id}/profile"
#     resource = APIResource.create(path=path, method="GET", schema={})

#     assert resource.title == "api_v1_users__user_id__profile"


# @patch("domain.entities.resources.NewAPIResourceCreatedEvent")
# def test_api_resource_triggers_domain_event(mock_event_cls):
#     """Проверяем только генерацию и регистрацию доменного события для APIResource."""
#     mock_event_instance = MagicMock()
#     mock_event_cls.return_value = mock_event_instance

#     path = "/api/v1/users/{user_id}/profile"
#     resource = APIResource.create(path=path, method="GET", schema={})

#     mock_event_cls.assert_called_once_with(
#         api_resource_oid=resource.oid,
#         api_resource_title="api_v1_users__user_id__profile",
#     )
#     assert resource._events == [mock_event_instance]


# # =====================================================================
# # ControllerResource Tests
# # =====================================================================


# def test_controller_resource_fields_initialization():
#     """Проверяем корректную инициализацию полей ControllerResource."""
#     handlers_code = "def get(): pass"
#     resource = ControllerResource.create(handlers=handlers_code)

#     assert resource.handlers == handlers_code


# @patch("domain.entities.resources.NewControllerResourceCreatedEvent")
# def test_controller_resource_triggers_domain_event(mock_event_cls):
#     """Проверяем генерацию и регистрацию доменного события для ControllerResource."""
#     mock_event_instance = MagicMock()
#     mock_event_cls.return_value = mock_event_instance

#     resource = ControllerResource.create(handlers="def get(): pass")

#     mock_event_cls.assert_called_once_with(controller_resource_oid=resource.oid)
#     assert resource._events == [mock_event_instance]


# # =====================================================================
# # ViewResource Tests
# # =====================================================================


# def test_view_resource_fields_initialization():
#     """Проверяем корректную инициализацию полей ViewResource."""
#     template_code = "<h1>Hello</h1>"
#     resource = ViewResource.create(template=template_code)

#     assert resource.template == template_code


# @patch("domain.entities.resources.NewViewResourceCreatedEvent")
# def test_view_resource_triggers_domain_event(mock_event_cls):
#     """Проверяем генерацию и регистрацию доменного события для ViewResource."""
#     mock_event_instance = MagicMock()
#     mock_event_cls.return_value = mock_event_instance

#     resource = ViewResource.create(template="<h1>Hello</h1>")

#     mock_event_cls.assert_called_once_with(view_resource_oid=resource.oid)
#     assert resource._events == [mock_event_instance]


# # =====================================================================
# # MVCResourcesBundle Tests
# # =====================================================================


# def test_mvc_resources_bundle_fields_initialization():
#     """Проверяем корректную инициализацию полей и структуры сета в MVCResourcesBundle."""
#     mock_title = MagicMock()

#     bundle = MVCResourcesBundle.create_bundle(title=mock_title)

#     assert bundle.title == mock_title
#     assert isinstance(bundle.resources, set)
#     assert len(bundle.resources) == 0


# @patch("domain.entities.resources.NewMVCResourcesBundleCreatedEvent")
# def test_mvc_resources_bundle_triggers_domain_event(mock_event_cls):
#     """Проверяем генерацию и регистрацию доменного события для MVCResourcesBundle."""
#     mock_event_instance = MagicMock()
#     mock_event_cls.return_value = mock_event_instance

#     mock_title = MagicMock()
#     mock_title.as_generic_type.return_value = "Generic Bundle Title"

#     bundle = MVCResourcesBundle.create_bundle(title=mock_title)

#     mock_event_cls.assert_called_once_with(
#         bundle_oid=bundle.oid, bundle_title="Generic Bundle Title"
#     )
#     assert bundle._events == [mock_event_instance]
