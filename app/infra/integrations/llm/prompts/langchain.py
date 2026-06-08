from dataclasses import dataclass

from infra.integrations.llm.prompts.base import BaseLLMPrompt




@dataclass
class LangchainLLMPrompt(BaseLLMPrompt):
    async def build_chain(
        prompt_template,
        structured_llm,
    ) -> :
        structured_llm = self.llm_instance.instance.with_structured_output(
            output_schema
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", settings.llm.prompts.system_prompt),
                ("user", settings.llm.prompts.system_prompt),
            ]
        )

        chain = prompt | structured_llm
