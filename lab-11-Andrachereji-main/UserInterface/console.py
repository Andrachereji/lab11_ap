from Service.boardgame_service import BoardgameService
from Service.sesiongame_service import SessiongameService


class Console:
    def __init__(self,
                 boardgame_service: BoardgameService,
                 sessiongame_service: SessiongameService):
        self.boardgame_service = boardgame_service
        self.sessiongame_service = sessiongame_service

    def show_menu(self):
        print('1.Adaugare boardgame')
        print('2.Adaugare sesiune joc')
        print('sb.Afisare boardinggame')
        print('ss.Afisare sesiune joc')
        print('3.Ordonarea dupa numarul maxim de jucatori '
              'cu tipul citit de la tastatura')
        print('4.ordonarea descrescatoare a brdgamurilor '
              'dupa numarul de jucatori care au jucat')
        print('5.Export json')
        print('x.Exit')

    def run_console(self):
        while True:
            self.show_menu()
            opt = input('Optiunea: ')
            if opt == '1':
                self.handle_add_boardgame()
            elif opt == 'sb':
                self.handle_show_all(self.boardgame_service.get_all())
            elif opt == '2':
                self.handle_add_sessiongame()
            elif opt == 'ss':
                self.handle_show_all(self.sessiongame_service.get_all())
            elif opt == '3':
                type = input('dati tipul:(competitiv/cooperativ')
                result = self.boardgame_service.\
                    get_boardgame_orderd_by_nr_max_player(type)
                self.handle_show_all(result)
            elif opt == '4':
                result = self.sessiongame_service.\
                    get_boardgame_orderd_by_number_of_players()
                self.handle_show_all(result)
            elif opt == '5':
                self.handle_export()
            elif opt == 'x':
                break
            else:
                print('Optiune invalida!')

    def handle_show_all(self, entities):
        for entity in entities:
            print(entity)

    def handle_add_boardgame(self):
        try:
            id_boardgame = input('id-ul boardgame-ului: ')
            name = input('Numele boardgame-ului: ')
            nr_minim_player = int(input('Numarul minim de jucatori: '))
            nr_maxim_player = int(input('Numarul maxim de jucatori: '))
            type = input('Tipul boardgame-ului (competitiv|cooperativ): ')
            self.boardgame_service.add_boardgame(id_boardgame, name,
                                                 nr_minim_player,
                                                 nr_maxim_player, type)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_add_sessiongame(self):
        try:
            id = input('Dati id-ul sesiunii')
            id_boardgame = input('id-ul boardgame-ului: ')
            nr_player = int(input('Dati numarul de jucatori: '))
            start_hour = input('Ora de inceput: ')
            stop_hour = input('Ora de sfarsit: ')
            winner_name = input('numele castigatorului: ')
            self.sessiongame_service.add_sessiongame(id, id_boardgame,
                                                     nr_player,
                                                     start_hour,
                                                     stop_hour,
                                                     winner_name)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_export(self):
            try:
                filename = input('Numele fisierului pentru export: ')
                self.sessiongame_service.export_json(filename)
            except Exception as ex:
                print('Eroare:', ex)
