from abc import ABC, abstractmethod
from asyncio import Semaphore
from dataclasses import dataclass


@dataclass
class BaseOpenAPIClient(ABC):
    @abstractmethod
    async def load_openapi_spec(self): ...
