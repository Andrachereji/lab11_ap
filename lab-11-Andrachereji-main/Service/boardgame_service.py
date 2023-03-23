from typing import List

from Domain.boardgame import Boardgame
from Domain.boardgame_validator import BoardgameValidator
from Repository.repository import Repository


class BoardgameService:
    def __init__(self,
                 boardgame_repository: Repository,
                 boardgame_validator: BoardgameValidator):
        '''
        Creeaza un service pentru boardgame-uri
        :param boardgame_repository:repository-ul boardgame-urilor
        :param boardgame_validator: validatorul pentru boardgame
        '''
        self.boardgame_repository = boardgame_repository
        self.boardgame_validator = boardgame_validator

    def add_boardgame(self, id_boardgame, name, nr_minim_player, nr_max_player, type):
        '''
        Adauga un boardgame
        :param id_boardgame: id-ul boargame-ului
        :param name: numele
        :param nr_minim_player: numarul minim de jucatori
        :param nr_max_player: numarul maxim de jucatori
        :param type: tipul
        '''
        boardgame = Boardgame(id_boardgame, name, nr_minim_player, nr_max_player, type)
        self.boardgame_validator.validate(boardgame)
        self.boardgame_repository.create(boardgame)

    def get_all(self) -> List[Boardgame]:
        '''
        :return: o lista cu toate boardgame-urile
        '''
        return self.boardgame_repository.read()
    def get_boardgame_orderd_by_nr_max_player(self, type):
        '''
        Ordonarea dupa numarul maxim de jucatori cu tipul
        citit de la tastatura
        :param type:tipul citit
        :return:lista ordonata cu prorietatile cerute
        '''
        result = []
        bordgames = self.get_all()
        for bordgame in bordgames:
            if bordgame.type == type:
                result.append((bordgame.name, bordgame.nr_max_player))
        return sorted(result, key=lambda x:x[1], reverse=True)