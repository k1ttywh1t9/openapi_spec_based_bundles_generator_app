from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class OpenAPISpecException(ApplicationException):
    message: str | None

    @property
    def message(self):
        return f"An OpenAPI Spec error occured. {self.message}"
