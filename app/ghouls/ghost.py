from .base import Ghoul, GhoulType


class Ghost(Ghoul):
    def __init__(self, name: str):
        super().__init__(name=name, ghoul_type=GhoulType.GHOST, spook_level=30)

    def scare(self):
        return f"{self.ooo()}... it's a spooky, spooky ghost!"
