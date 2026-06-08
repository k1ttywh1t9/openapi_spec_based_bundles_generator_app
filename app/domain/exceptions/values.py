from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'Too long title text "{self.text[:255]}..."'


@dataclass(eq=False)
class EmptyTextException(ApplicationException):
    text: str | None = None

    @property
    def message(self):
        return f"Empty text application error occured. {self.text}"


@dataclass(eq=False)
class InvalidCodeSyntaxException(ApplicationException):
    text: str | None = None

    @property
    def message(self):
        return f"Invalid Code Syntax application error occured. \n {self.text}"
