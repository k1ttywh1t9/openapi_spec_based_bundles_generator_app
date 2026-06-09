from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class OpenAPISpecWithThatTitleAlreadyExistsException(LogicException):
    title: str

    @property
    def message(self):
        return f'OpenAPI Specification with title: "{self.title}" alredy exists.'


@dataclass(eq=False)
class OpenAPINotFoundException(LogicException):
    spec_oid: str

    @property
    def message(self):
        return f"Open API Spec with {self.chat_oid=} not found."
