from Domain.boardgame_validator import BoardgameValidator
from Repository.json_repository import JsonRepository
from Service.boardgame_service import BoardgameService
from Service.sesiongame_service import SessiongameService
from UserInterface.console import Console


def main():
    boardgame_repository = JsonRepository('boardgame.json')
    sessiongame_repository = JsonRepository('sessiongame.json')
    boardgame_validator = BoardgameValidator()
    boardgame_service = BoardgameService(boardgame_repository, boardgame_validator)
    sessiongame_service = SessiongameService(sessiongame_repository, boardgame_repository)
    console = Console(boardgame_service, sessiongame_service)
    console.run_console()


if __name__ == '__main__':
    main()
