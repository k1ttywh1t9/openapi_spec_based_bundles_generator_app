from pathlib import Path

from pydantic import (
    BaseModel,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent

# define absolute path to .env
DOTENV_PATH: Path = BASE_DIR / ".env"
DOTENV_EXAMPLE_PATH: Path = BASE_DIR / ".env.example"


class LLMConfig(BaseModel):
    api_key: str
    api_base_url: str
    model: str


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
    openapi: OpenAPIConfig


settings = Settings()
