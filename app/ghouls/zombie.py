import random

from .base import Ghoul, GhoulType


class Zombie(Ghoul):
    def __init__(self, name: str, level_of_decay: int):
        self.level_of_decay = level_of_decay
        super().__init__(name=name, ghoul_type=GhoulType.ZOMBIE, spook_level=4)

    def growl(self) -> str:
        random.seed(self._seed)
        return "U" + "".join(random.choices(population="hH", k=self.level_of_decay * 3))

    def scare(self):
        return f"{self.growl()}... brains (probably)!"
