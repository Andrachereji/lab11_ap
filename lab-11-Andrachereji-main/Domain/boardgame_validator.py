from Domain.boardgame import Boardgame


class BoardgameValidator:
    '''
    Validator pentru boardgame-uri
    :return erori daca exista
    '''
    def validate(self,
                 game: Boardgame):
        errors = []
        if game.nr_max_player < 0:
            errors.append('Numarul trebuie sa fie pozitiv')
        if game.nr_minim_player < 0:
            errors.append('Numarul trebuie sa fie pozitiv')
        if game.type not in ['competitiv', 'cooperativ']:
            errors.append('tipul este invalid')
        if errors:
            raise ValueError(errors)
