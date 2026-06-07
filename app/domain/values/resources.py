from dataclasses import dataclass
from enum import Enum

from domain.exceptions.message import (
    EmptyTextException,
    TitleTooLongException,
)
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class ArtifactType(Enum):
    ROUTER = "router"
    SCHEMA = "schema"
    TEMPLATE = "template"
    CSS = "css"


@dataclass(frozen=True)
class CodeContent:
    body: str
    lang: str
    checksum: str

    def as_generic_type(self) -> VT: ...


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
