from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from domain.events.base import BaseEvent
from logic.mediator.base.command import CommandMediator


@dataclass
class IntegrationEvent(BaseEvent, ABC): ...


ET = TypeVar("ET", bound=IntegrationEvent)
ER = TypeVar("ER", bound=Any)


@dataclass
class IntegrationEventHandler(ABC, Generic[ET, ER]):
    _mediator: CommandMediator

    @abstractmethod
    async def handle(self, event: ET) -> ER: ...
