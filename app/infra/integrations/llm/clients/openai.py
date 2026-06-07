from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type

from langchain_openai import ChatOpenAI

from settings.main import settings
from infra.integrations.llm.base import BaseLLMClient
from infra.integrations.llm.models.base import OpenAILLMInstance
from infra.integrations.llm.models.base import BaseLLMInstance


@dataclass
class OpenAILLMClient(BaseLLMClient):
    llm_instance: OpenAILLMInstance
    
    async def invoke_request(self, prompt: output_schema: Type[T]) -> T:
        structured_llm = self.llm_instance.instance.with_structured_output(
            output_schema,
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", settings.llm.prompts.system_prompt),
                ("user", settings.llm.prompts.system_prompt),
            ]
        )

        chain = prompt | structured_llm
        return await chain.ainvoke(prompt_vars)
