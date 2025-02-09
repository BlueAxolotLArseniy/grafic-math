from enum import Enum, auto


class PlayerState(Enum):
    active = auto()
    dead = auto()
    respawn = auto()
