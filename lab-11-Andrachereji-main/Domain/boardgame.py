from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Boardgame(Entity):
    name: str
    nr_minim_player: int
    nr_max_player: int
    type: str

