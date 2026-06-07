from abc import ABC, abstractmethod
from dataclasses import dataclass

from langchain_openai import ChatOpenAI

from app.infra.integrations.llm.models.openai import (
    BaseLLMInstance,
    BaseLLMRequest,
    BaseLLMResponse,
)


@dataclass
class OpenAILLMRequest(BaseLLMRequest): ...


@dataclass
class OpenAILLMResponse(BaseLLMResponse): ...


@dataclass
class OpenAILLMInstance(BaseLLMInstance):
    instance: ChatOpenAI
