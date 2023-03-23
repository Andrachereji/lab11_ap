from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class SessionGame(Entity):
    id_boardgame: str
    player_number: int
    start_hour: str
    stop_hour: str
    name_winner: str
