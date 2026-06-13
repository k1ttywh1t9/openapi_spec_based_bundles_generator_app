from pathlib import Path

from pydantic import (
    BaseModel,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

from settings.llm import LLMConfig

BASE_DIR = Path(__file__).parent.parent.parent

# define absolute path to .env
DOTENV_PATH: Path = BASE_DIR / ".env"
DOTENV_EXAMPLE_PATH: Path = BASE_DIR / ".env.example"


class MessageBrokerTopicsConfig(BaseModel):
    new_openapi_spec_entity_created_topic: str = "new_openapi_spec_entity_created_topic"
    openapi_spec_entity_received_event_topic: str = (
        "openapi_spec_entity_received_event_topic"
    )


class MessageBrokerConfig(BaseModel):
    topics: MessageBrokerTopicsConfig = MessageBrokerTopicsConfig()


class OpenAPIConfig(BaseModel):
    path: str | None = None
    url: str | None = None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(DOTENV_PATH,),
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        extra="allow",
    )

    llm: LLMConfig
    message_broker: MessageBrokerConfig = MessageBrokerConfig()
    openapi: OpenAPIConfig = OpenAPIConfig()
