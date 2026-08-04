from service.game import Game
from service.data import data_control


MENUS = {
        1: ("퀴즈 풀기", Game.play),
        2: ("퀴즈 추가", Game.add),
        3: ("퀴즈 목록", Game.list),
        4: ("점수 확인", Game.score),
        5: ("종료", Game.exit),
    }

def run_start():
    data = data_control.load_data()

    while True:
        print("\n나만의 퀴즈게임\n 메뉴를 선택해주세요.")
        for k, (t, _) in MENUS.items():
            print(f'{k}. {t}')

        try:
            menu_selected = int(input("메뉴 선택: ").strip())

            if menu_selected in MENUS:
                title, func = MENUS[menu_selected]
                result = func(data)
                if result is False:
                    break

        except ValueError: 
            print("잘못된 입력입니다. 1-5 사이의 숫자로 입력해주세요.")

