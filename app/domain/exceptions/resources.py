from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class APIResourceException(ApplicationException):
    message: str | None

    @property
    def message(self):
        return f"An APIResource error occured. {self.message}"


@dataclass(eq=False)
class UIResourceException(ApplicationException):
    message: str | None

    @property
    def message(self):
        return f"An UIResource error occured. {self.message}"
