from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class BaseLLMRequest(ABC): ...

@dataclass
class BaseLLMResponse(ABC): ...

@dataclass
class BaseLLMInstance(ABC): ...
