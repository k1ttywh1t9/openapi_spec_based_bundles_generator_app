from pydantic import BaseModel, Field
from typing import List


# Описываем структуру, которую хотим получить на выходе
class CodeArtifact(BaseModel):
    filename: str = Field(
        description="Имя файла, например: schemas.py или pet_service.py"
    )
    code: str = Field(description="Полный, готовый к использованию код (Python/Jinja2)")
    explanation: str = Field(description="Краткое пояснение реализации")


class GenerationResponse(BaseModel):
    artifacts: List[CodeArtifact] = Field(description="Список сгенерированных файлов")
