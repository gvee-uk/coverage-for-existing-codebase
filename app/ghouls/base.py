import random
from abc import ABC, abstractmethod
from enum import StrEnum, auto


class GhoulType(StrEnum):
    GHOST = auto()
    ZOMBIE = auto()


class Ghoul(ABC):
    def __init__(self, name: str, ghoul_type: GhoulType, spook_level: int = 0) -> None:
        self.name = name
        self.ghoul_type = ghoul_type
        self.spook_level = spook_level

    @property
    def _seed(self) -> int:
        return f"{self.ghoul_type} + {self.name} + {self.spook_level}"

    def introduce(self) -> str:
        return f"Hello, my name is {self.name} and I'm a {self.ghoul_type}."

    def ooo(self) -> str:
        """A [somewhat] deterministic spooky sound that each ghoul makes."""
        random.seed(self._seed)
        return "".join(random.choices(population="Oo", k=self.spook_level))

    @abstractmethod
    def scare(self) -> str:
        pass
