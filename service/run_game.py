
    

from service.quiz import Quiz
from service.data import data_control


def game_play(data):
    print("게임을 시작합니다.\n")

    quizzes = data["quizzes"]
    score = 0

    for i, q in enumerate(quizzes, start=1):
        quiz = Quiz(q["question"], q["choices"], q["answer"])

        quiz.display(i)

        user_answer = int(input("정답은 : ").strip())

        if quiz.check_answer(user_answer):
            print("정답입니다.")
            score += 10
        else:
            print(f"틀렸습니다. 정답은: {quiz.answer}번 {quiz.choices[quiz.answer-1]}")
    print(f"\n 최종 점수 : {score}")


def game_add(data):
    print("문제를 추가합니다.")

def game_list(data):
    print("문제 리스트를 조회합니다.")
    
def game_score(data):
    print("점수를 조회합니다.")

def game_exit(data):
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

