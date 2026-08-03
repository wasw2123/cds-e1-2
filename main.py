from service.run_game import run_start


if __name__ == "__main__":
    try:
        run_start()
    except (KeyboardInterrupt, EOFError):
        # data_save()
        print("현재 상황을 저장하고 게임을 종료합니다.")
