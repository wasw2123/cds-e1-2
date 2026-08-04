from random import randint

from service.data import data_control
from service.quiz import Quiz


class QuizGame:
    def __init__(self):
        self.data = data_control.load_data()
        self.quizzes = self.data.get("quizzes")
        self.best_score = self.data.get("best_score")
        self.MENUS = {
            1: ("퀴즈 풀기", self.play),
            2: ("퀴즈 추가", self.add),
            3: ("퀴즈 목록", self.list),
            4: ("점수 확인", self.score),
            5: ("종료", self.exit),
        }
        self.FULL_SCORE = 10
        self.HINT_SCORE = 9
        self.HINT_OPTION = 5


    def menu(self):
        print("\n나만의 퀴즈게임\n 메뉴를 선택해주세요.")
        for k, (t, _) in self.MENUS.items():
            print(f'{k}. {t}')

        try:
            menu_selected = int(input("메뉴 선택: ").strip())

            if menu_selected in self.MENUS:
                _, func = self.MENUS[menu_selected]
                result = func()
                if result is False:
                    return False

        except ValueError: 
            print("잘못된 입력입니다. 메뉴와 매칭되는 숫자를 입력해주세요.")

    
    def play(self) -> None:
        print("게임을 시작합니다.\n")

        quizzes = self.quizzes
        if not quizzes:
            data_control.quiz_data_reset(self.data)
            return

        print("몇 문제를 풀지 선택해주세요. (최대 10문제)")
        while True:
            try:
                num_questions = int(input("문제 수: ").strip())
                if num_questions < 1 or num_questions > 10:
                    print("1 이상 10 이하의 숫자를 입력해주세요.")
                else:
                    break
            except ValueError:
                print("잘못된 입력입니다. 1-10 사이의 숫자를 입력해주세요.")

        min_questions = min(10, len(quizzes), num_questions)
        print("-----------------------")
        print(f"\n총 {min_questions}문제를 풀게 됩니다. 시작합니다!\n")
        print("-----------------------")

        score = 0
        selected_indices = []
        for _ in range(min_questions):
            idx = randint(0, len(quizzes) - 1)
            while idx in selected_indices:
                idx = randint(0, len(quizzes) - 1)
            selected_indices.append(idx)

        for i, q in enumerate(selected_indices, start=1):
            quiz = Quiz(quizzes[q]["question"], quizzes[q]["choices"], quizzes[q]["answer"], quizzes[q].get("hint", "힌트가 없습니다."))

            quiz.display(i)

            user_answer = self._get_user_answer()

            point = self.FULL_SCORE
            if user_answer == self.HINT_OPTION:
                print("힌트 : ", quiz.hint)
                point = self.HINT_SCORE
                user_answer = self._get_user_answer()

            if quiz.check_answer(user_answer):
                score += point
                print(f"정답입니다. {point}점 획득")
            else:
                print(f"틀렸습니다. 정답은: {quiz.answer}번 {quiz.choices[quiz.answer-1]}")

        print(f"\n 최종 점수 : {score}")

        best_score = self.best_score
        if best_score < score:
            self.data["best_score"] = score
            print("최고 점수가 갱신됐습니다.")


    def add(self):
        print("문제를 추가합니다.")
        question = input("문제를 입력하세요 : ").strip()

        choices = []
        choice_range = range(1, 5)
        for i in choice_range:
            c = input(f"선택지 {i}번 : ").strip()
            choices.append(c)

        answer = 0
        while answer not in choice_range:
            try:
                answer = int(input("정답 번호(1-4) : ").strip())
            except ValueError:
                print("숫자가 아닌 값을 입력하셨습니다. 정답은 숫자(1-4)로 입력해주세요.")
            else:
                if answer not in choice_range:
                    print("정답은 숫자 중 1-4 사이에서 입력해주세요.")
        

        new_quiz = {
            "question": question,
            "choices": choices,
            "answer": answer,
        }

        print("문제가 맞는지 확인해 주세요.")
        print("---------------------")
        print(f"[문제] {new_quiz['question']}")
        for i, c in enumerate(new_quiz["choices"], start=1):
            print(f"{i}. {c}")
        print(f"정답 : {new_quiz['answer']}")

        checker = input("맞으면 1번 틀리면 다른 아무 문자를 입력해주세요 : ")
        if not checker == "1":
            print("문제를 저장하지 않고 메뉴로 돌아갑니다.")
            return
        self.data["quizzes"].append(new_quiz)
        data_control.save_data(self.data)
        print("퀴즈를 추가하였습니다. 메뉴로 돌아갑니다.")



    def list(self):
        print("문제 리스트를 조회합니다.")
        print("---------------------")

        quizzes = self.quizzes
        if not quizzes:
            data_control.quiz_data_reset(self.data)
            return

        for i, q in enumerate(quizzes, start=1):
            quiz = Quiz(q["question"], q["choices"], q["answer"])

            quiz.display(i)
            print(f"\n정답 : {q['answer']}")

        print(f"\n총 문제 수 : {len(quizzes)}")
        
    def score(self):
        print(f"현재 최고 점수는 {self.best_score}입니다")

    def exit(self):
        data_control.save_data(self.data)
        print("현재 상태를 저장하고 게임을 종료합니다.")

        return False


    def _get_user_answer():
        try:
            user_answer = int(input("정답은 : ").strip())
        except ValueError:
            user_answer = -1
        return user_answer

game = QuizGame()