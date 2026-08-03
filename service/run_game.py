
def game_play():
    print("게임을 시작합니다.")

def game_add():
    print("문제를 추가합니다.")

def game_list():
    print("문제 리스트를 조회합니다.")
    
def game_score():
    print("점수를 조회합니다.")

def game_exit():
    print("게임을 종료합니다.")

    return False



MENUS = {
        1: ("퀴즈 풀기", game_play),
        2: ("퀴즈 추가", game_add),
        3: ("퀴즈 목록", game_list),
        4: ("점수 확인", game_score),
        5: ("종료", game_exit),
    }

def run_start():
    while True:
        print("\n나만의 퀴즈게임\n 메뉴를 선택해주세요.")
        for k, (t, _) in MENUS.items():
            print(f'{k}. {t}')

        try:
            menu_selected = int(input("메뉴 선택: ").strip())

            if menu_selected in MENUS:
                title, func = MENUS[menu_selected]
                result = func()
                if result is False:
                    break

        except ValueError: 
            print("잘못된 입력입니다. 1-5 사이의 숫자로 입력해주세요.")

