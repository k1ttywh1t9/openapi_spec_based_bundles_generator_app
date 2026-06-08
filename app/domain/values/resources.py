import ast
from dataclasses import dataclass
from enum import Enum
import hashlib
from typing import NamedTuple, Self
from domain.exceptions.values import (
    EmptyTextException,
    InvalidCodeSyntaxException,
    TitleTooLongException,
)
from domain.values.base import VT, BaseValueObject


@dataclass(frozen=True)
class ArtifactType(Enum):
    ROUTER = "router"
    SCHEMA = "schema"
    TEMPLATE = "template"
    CSS = "css"


class CodeState(NamedTuple):
    body: str
    lang: str
    checksum: str


@dataclass(frozen=True)
class CodeContent(BaseValueObject[CodeState]):
    def validate(self):
        """Local content validation."""
        body = self.value.body

        if not body or not body.strip():
            raise EmptyTextException("Controller Code cannot be empty.")

        if self.value.lang.lower() == "python":
            try:
                ast.parse(body)
            except SyntaxError as e:
                raise InvalidCodeSyntaxException(
                    f"Invalid Python syntax has been given: {e.msg}"
                    f"(str {e.lineno}, position {e.offset})"
                ) from e

    @classmethod
    def from_raw(cls, body: str, lang: str = "python") -> Self:
        """Factory method w/ normalizing."""
        normalized_body = body.replace("\r\n", "\n")

        bytes_code = normalized_body.encode("utf-8")
        checksum = hashlib.sha256(bytes_code).hexdigest()

        state = CodeState(body=normalized_body, lang=lang.lower(), checksum=checksum)
        return cls(value=state)

    @property
    def body(self) -> str:
        return self.value.body

    @property
    def lang(self) -> str:
        return self.value.lang

    @property
    def checksum(self) -> str:
        return self.value.checksum

    def as_generic_type(self) -> dict:
        return {
            "body": self.value.body,
            "lang": self.value.lang,
            "checksum": self.value.checksum,
        }


@dataclass(frozen=True)
class ResourceIdentifier:
    entity_id: str
    module: str
    version: str


@dataclass(frozen=True)
class Text(BaseValueObject[str]):
    def validate(self):
        if not self.value:
            raise EmptyTextException()

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Title(BaseValueObject[str]):
    def validate(self):
        if not self.value:
            raise EmptyTextException()

        if len(self.value) > 255:
            raise TitleTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)
