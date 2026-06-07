from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

from domain.entities.bundles import Bundle
from domain.entities.messages import Chat, Message
from infra.repositories.filters.messages import GetAllChatsFilters, GetMessagesFilters


@dataclass
class BaseBundlesRepository(ABC):
    @abstractmethod
    async def check_bundle_exists_by_title(self, title: str) -> bool: ...

    @abstractmethod
    async def get_bundle_by_oid(self, oid: str) -> Bundle | None: ...

    @abstractmethod
    async def add_bundle(self, bundle: Bundle) -> None: ...

    # @abstractmethod
    # async def get_all_bundles(
    #     self, fitlers: GetAllBundlesFilters
    # ) -> Iterable[bundle]: ...


@dataclass
class BaseResourcesRepository(ABC):
    @abstractmethod
    async def add_resource(self, message: Message) -> None: ...

    @abstractmethod
    async def get_resources(
        self,
        chat_oid: str,
        filters: GetMessagesFilters,
    ) -> tuple[Iterable[Message], int]: ...
