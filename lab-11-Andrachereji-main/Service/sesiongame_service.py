import json
from typing import List

from Domain.sesiongame import SessionGame
from Repository.repository import Repository
from view_models.bordergame_with_players import BordgameWithPlayers


class SessiongameService:
    def __init__(self,
                 sessiongame_repository: Repository,
                 boardgame_repository: Repository):
        '''
        Creeaza un service pentru sesiunea de jocuri
        :param sessiongame_repository:repository-ul sesiunilor
        :param boardgame_repository: repository-ul bardgame-urilor
        '''
        self.sessiongame_repository = sessiongame_repository
        self.boardgame_repository = boardgame_repository

    def add_sessiongame(self, id, id_boardgame, player_number, start_hour, stop_hour, name_winner):
        '''
        Adauga o sesiune de joc
        :param id: id-ul sesiunii
        :param id_boardgame: id-ul boardgame-ului
        :param player_number: numar jucatori
        :param start_hour: inceputul jocului
        :param stop_hour: sfarsitul jocului
        :param name_winner: numele castigatorului
        '''
        sessiongame = SessionGame(id, id_boardgame, player_number, start_hour, stop_hour, name_winner)
        errors = []
        if self.boardgame_repository.read(id_boardgame) is None:
            errors.append('Acest joc nu este inregistrat')
        if player_number > self.boardgame_repository.read(id_boardgame).nr_max_player:
            errors.append('Prea multi jucatori')
        if player_number < self.boardgame_repository.read(id_boardgame).nr_minim_player:
            errors.append('Prea putini jucatori')
        if errors:
            raise ValueError(errors)
        self.sessiongame_repository.create(sessiongame)


    def get_all(self) -> List[SessionGame]:
        '''
        :return: o lista cu toate sesiunile
        '''
        return self.sessiongame_repository.read()
    def get_boardgame_orderd_by_number_of_players(self):
        '''
        ordonarea descrescatoare a brdgamurilor dupa numarul
        de jucatori care au jucat
        :return:
        '''
        result = []
        for bordgame in self.boardgame_repository.read():
            nr_players = 0
            for sessiongame in self.get_all():
                if sessiongame.id_boardgame == bordgame.id_entity:
                    nr_players = nr_players + sessiongame.player_number
            bordgame_with_players = BordgameWithPlayers(bordgame.id_entity, bordgame, nr_players)
            result.append(bordgame_with_players)
        return sorted(result, key=lambda x: x.number_of_players, reverse=True)

    def export_json(self, export_filename):
        '''
        Se creaza un fisier JSON in care cheile sunt
        numele jucatorilor ce au castigat
        cel putin o sesiune de joc ,iar valorile sunt
        liste cu numele boardgame-urlior castigate
        :param export_filename: numele fisierului in care se exporta
        '''
        result = {}
        sessiongames = self.sessiongame_repository.read()
        for sessiongame in sessiongames:
            result[sessiongame.name_winner] = [bordgame.name for bordgame in self.boardgame_repository.read()
                                               if bordgame.id_entity == sessiongame.id_boardgame]
        with open(export_filename, 'w') as f:
            json.dump(result, f, indent=2)
