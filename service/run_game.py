from service.game import game


def run():
    try:
        while True:
            status = game.menu()
            if status is False:
                break

    except (KeyboardInterrupt, EOFError):
        game.save()
        print("\n현재 상황을 저장하고 게임을 종료합니다.")

