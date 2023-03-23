from dataclasses import dataclass

from Domain.boardgame import Boardgame

@dataclass
class BordgameWithPlayers:
    id: str
    bordergame: Boardgame
    number_of_players: int