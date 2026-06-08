from unittest.mock import MagicMock, patch

from domain.entities.resources import ControllerResource


def test_controller_resource_creation_fields_initialization():
    """Testing ControllerResource fields correct initialization."""

    lang = "python"
    handlers_code = """
import asyncio

async def get(): 
    pass
    
async def main():
    await get()
    
if __name__ == "__main__":
    asyncio.run(main())

    """
    resource = ControllerResource.create(handlers=handlers_code, lang=lang)

    assert resource.handlers.lang == lang
    assert resource.handlers.body == handlers_code


@patch("domain.entities.resources.NewControllerResourceCreatedEvent")
def test_controller_resource_creation_triggers_domain_event(mock_event_cls):
    """Testing ControllerResource domain event generation and registration."""
    mock_event_instance = MagicMock()
    mock_event_cls.return_value = mock_event_instance

    lang = "python"
    handlers_code = """
import asyncio

async def get(): 
    pass
    
async def main():
    await get()
    
if __name__ == "__main__":
    asyncio.run(main())

    """

    resource = ControllerResource.create(handlers=handlers_code, lang=lang)

    mock_event_cls.assert_called_once_with(controller_resource_oid=resource.oid)
    assert resource._events == [mock_event_instance]
