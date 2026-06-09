from dataclasses import dataclass, field
from typing import Generic, Iterable, TypeVar

from infra.repositories.base import ET, FT, BaseRepository


@dataclass
class MemoryRepository(BaseRepository[ET, FT]):
    _saved_items: list[ET] = field(default_factory=list, kw_only=True)

    async def get_item_by_oid(self, oid: str) -> ET | None:
        try:
            return next(
                item for item in self._saved_items if getattr(item, "oid", None) == oid
            )
        except StopIteration:
            return None

    async def add_item(self, item: ET) -> None:
        self._saved_items.append(item)

    async def get_all_items(self, filters: FT) -> Iterable[ET]:
        offset = getattr(filters, "offset")
        limit = getattr(filters, "limit")

        return self._saved_items[offset : offset + limit]
