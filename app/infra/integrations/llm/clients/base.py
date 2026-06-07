from abc import ABC, abstractmethod
from dataclasses import dataclass

from infra.integrations.llm.models.base import BaseLLMInstance


@dataclass
class BaseLLMClient(ABC):
    @abstractmethod
    async def invoke_request() -> None: ...


# from agent.prompts import SYSTEM_PROMPT, USER_PROMPT
# from agent.responses import GenerationResponse
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from core.config import settings

# # Инициализация модели
# llm = ChatOpenAI(
#     model=settings.llm.model,
#     base_url=settings.llm.api_base_url,
#     api_key=settings.llm.api_key,
#     temperature=0,
#     max_retries=3,
#     max_tokens=2000,
# )

# # Привязываем модель к нашей схеме
# structured_llm = llm.with_structured_output(GenerationResponse)

# # Создаем шаблон
# prompt_template = ChatPromptTemplate.from_messages(
#     [("system", SYSTEM_PROMPT), ("user", USER_PROMPT)]
# )

# # Цепочка готова к .ainvoke()
# chain = prompt_template | structured_llm
