from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Generic, TypeVar

ET = TypeVar("ET")
FT = TypeVar("FT")


@dataclass
class BaseRepository(ABC, Generic[ET, FT]):

    @abstractmethod
    async def get_item_by_oid(self, oid: str) -> ET | None: ...

    @abstractmethod
    async def add_item(self, item: ET) -> None: ...

    @abstractmethod
    async def get_all_items(self, filters: FT) -> Iterable[ET]: ...
