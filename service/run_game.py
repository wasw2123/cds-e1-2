from service.game import game
from service.data import data_control


def run():
    try:
        while True:
            status = game.menu()
            if status is False:
                break

    except (KeyboardInterrupt, EOFError):
        data_control.save_data(game.data)
        print("\n현재 상황을 저장하고 게임을 종료합니다.")

