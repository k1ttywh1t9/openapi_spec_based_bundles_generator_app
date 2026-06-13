from pydantic import BaseModel


class OpenAILLMConfig(BaseModel):
    temperature: float = 0
    max_retries: int = 3
    max_tokens: int = 2000
    api_key: str
    api_base_url: str
    model: str


class PromptLLMConfig(BaseModel):
    system_prompt: str = """
You are a Senior FastAPI and Jinja2 Architect. Your task is to generate modular, high-quality code based on OpenAPI specifications.

Adhere to these strict guidelines:
1. DRY (Don't Repeat Yourself): Use Pydantic models for request validation and schema definition.
2. Security: Always use FastAPI's `TemplateResponse` for rendering HTML.
3. Modularity: Each router must be isolated in its own file and handle only one domain entity.
4. Precision: Use ONLY the provided OpenAPI chunk. Do not guess field types; if a schema is incomplete, infer logical defaults but add a comment noting the assumption.
5. Formatting: Output MUST be a valid JSON object matching the requested schema. No conversational filler.
6. File Paths: Always include a relative path in filename field. Use the structure: routers/{entity_name}/... or schemas/{entity_name}.py.
7. Naming Convention: If the entity name is longer than 20 characters, create a short, snake_case alias for the folder name. Always output the alias in the filename field. Keep directory paths short.
"""
    user_prompt: str = """
Goal: Generate a FastAPI router and a corresponding Jinja2 HTML template for the entity: {entity_name}.

Context (OpenAPI Fragment):
{openapi_chunk}

Technical Requirements:
- The router must use `APIRouter` with appropriate prefixing.
- Generate Pydantic models derived strictly from the provided OpenAPI schema.
- The HTML template must include a data table for GET requests and a form for POST requests.
- Use Jinja2 syntax compatible with FastAPI's `TemplateResponse`.

Return the response in the specified JSON structure.
"""


class LLMConfig(BaseModel):
    prompts: PromptLLMConfig = PromptLLMConfig()
    openai: OpenAILLMConfig
