import random
from datetime import datetime

from service.core import get_user_input
from service.data import data_control
from service.quiz import Quiz


class QuizGame:
    def __init__(self):
        self.data = data_control.load_data() or {}
        self.quizzes = self.data.setdefault("quizzes", [])
        self.best_score = self.data.setdefault("best_score", 0)
        self.history = self.data.setdefault("history", [])
        self.MENUS = {
            1: ("퀴즈 풀기", self.play),
            2: ("퀴즈 추가", self.add),
            3: ("퀴즈 목록", self.list),
            4: ("점수 확인", self.score),
            5: ("문제 삭제", self.delete),
            6: ("게임 기록 조회", self.get_history),
            0: ("종료", self.exit),
        }
        self.FULL_SCORE = 10
        self.HINT_SCORE = 9
        self.HINT_OPTION = 5

    def save(self):
        self.data["quizzes"] = self.quizzes
        self.data["best_score"] = self.best_score
        self.data["history"] = self.history
        data_control.save_data(self.data)


    def menu(self):
        print("\n나만의 퀴즈게임\n 메뉴를 선택해주세요.")
        for k, (t, _) in self.MENUS.items():
            print(f'{k}. {t}')

        try:
            menu_selected = int(input("메뉴 선택: ").strip())
            if menu_selected not in self.MENUS:
                print("잘못된 입력입니다. 메뉴와 매칭되는 숫자를 입력해주세요.")
                return

            if menu_selected in self.MENUS:
                _, func = self.MENUS[menu_selected]
                result = func()
                if result is False:
                    return False

        except ValueError: 
            print("잘못된 입력입니다. 메뉴와 매칭되는 숫자를 입력해주세요.")

    
    def play(self) -> None:
        print("게임을 시작합니다.\n")

        if not self.quizzes:
            self.quizzes = data_control.quiz_data_reset(self.data)
        quizzes = self.quizzes

        print("몇 문제를 풀지 선택해주세요. (최대 10문제)")
        while True:
            try:
                raw = get_user_input("문제 수: ")
                num_questions = int(raw)
                if num_questions < 1 or num_questions > 10:
                    print("1 이상 10 이하의 숫자를 입력해주세요.")
                else:
                    break
            except ValueError:
                print("잘못된 입력입니다. 1-10 사이의 숫자를 입력해주세요.")

        question_count = min(10, len(quizzes), num_questions)
        print("-----------------------")
        print(f"\n총 {question_count}문제를 풀게 됩니다. 시작합니다!\n")
        print("-----------------------")

        score = 0
        selected_indices = random.sample(self.quizzes, question_count)

        for i, q in enumerate(selected_indices, start=1):
            quiz = Quiz(q["question"], q["choices"], q["answer"], q.get("hint", "힌트가 없습니다."))

            quiz.display(i)

            user_answer = self._get_user_answer()

            point = self.FULL_SCORE
            if user_answer == self.HINT_OPTION:
                quiz.display_hint()
                point = self.HINT_SCORE
                user_answer = self._get_user_answer("정답은 (1-4) : ")

            if quiz.check_answer(user_answer):
                score += point
                print(f"정답입니다. {point}점 획득")
            else:
                print(f"틀렸습니다. 정답은: {quiz.answer}번 {quiz.choices[quiz.answer-1]}")

        print(f"\n 최종 점수 : {score}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({
            "timestamp": timestamp,
            "questions": question_count,
            "score": score
        })

        if self.best_score < score:
            self.best_score = score
            print("최고 점수가 갱신됐습니다.")
        self.save()


    def add(self):
        print("문제를 추가합니다.")
        question = get_user_input("문제 : ", msg = "문제를 비워둘 수 없습니다. 다시 입력해주세요.")
        choices = []
        choice_range = range(1, 5)
        for i in choice_range:
            c = get_user_input(f"선택지 {i} : ", msg = "선택지를 비워둘 수 없습니다. 다시 입력해주세요.")
            choices.append(c)

        hint = get_user_input("힌트 : ", msg = "힌트를 비워둘 수 없습니다. 다시 입력해주세요.")

        while True:
            try:
                raw = get_user_input("정답 (1-4) : ", msg = "정답을 비워둘 수 없습니다. 1-4 사이 숫자를 입력해주세요.")
                answer = int(raw)
                if answer not in choice_range:
                    print("정답은 숫자 중 1-4 사이에서 입력해주세요.")
                else:
                    break
            except ValueError:
                print("숫자가 아닌 값을 입력하셨습니다. 정답은 숫자(1-4)로 입력해주세요.")
            


        new_quiz = {
            "question": question,
            "choices": choices,
            "answer": answer,
            "hint": hint,
        }

        print("문제가 맞는지 확인해 주세요.")
        print("---------------------")
        print(f"[문제] {new_quiz['question']}")
        for i, c in enumerate(new_quiz["choices"], start=1):
            print(f"{i}. {c}")
        print("---------------------")
        print(f"힌트 : {new_quiz['hint']}\n")
        print(f"정답 : {new_quiz['answer']}")
        print("---------------------")
        checker = input("저장하시려면 1번 을 입력해주세요. (취소는 아무 키나 입력) : ").strip()
        if not checker == "1":
            print("문제를 저장하지 않고 메뉴로 돌아갑니다.")
            return
        self.quizzes.append(new_quiz)
        self.save()
        print("퀴즈를 추가하였습니다. 메뉴로 돌아갑니다.")



    def list(self):
        print("문제 리스트를 조회합니다.")
        print("---------------------")

        if not self.quizzes:
            self.quizzes = data_control.quiz_data_reset(self.data)
        quizzes = self.quizzes

        for i, q in enumerate(quizzes, start=1):
            quiz = Quiz(q["question"], q["choices"], q["answer"], q.get("hint", "힌트가 없습니다."))

            quiz.display(i)
            quiz.display_hint()
            print(f"\n정답 : {q['answer']}")

        print(f"\n총 문제 수 : {len(quizzes)}")
        
    def score(self):
        if not self.best_score and not self.history:
            print("아직 플레이 기록이 없습니다. 게임을 플레이하고 최고 점수를 기록해보세요.")
        else:
            print(f"현재 최고 점수는 {self.best_score}입니다")

    def exit(self):
        self.save()
        print("현재 상태를 저장하고 게임을 종료합니다.")

        return False

    def delete(self):
        print("문제를 삭제합니다.")
        if not self.quizzes:
            self.quizzes = data_control.quiz_data_reset(self.data)
        quizzes = self.quizzes

        for i, q in enumerate(quizzes, start=1):
            quiz = Quiz(q["question"], q["choices"], q["answer"], q.get("hint", "힌트가 없습니다."))
            quiz.display(i)
            quiz.display_hint()
            print(f"\n정답 : {q['answer']}")
            print("---------------------")

        while True:
            try:
                raw = get_user_input("삭제할 문제 번호를 입력해주세요. (취소는 0번) : ")
                delete_index = int(raw)
                if delete_index == 0:
                    print("삭제를 취소하고 메뉴로 돌아갑니다.")
                    return
                elif 1 <= delete_index <= len(quizzes):
                    break
                else:
                    print(f"1부터 {len(quizzes)} 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")

        deleted_quiz = quizzes.pop(delete_index - 1)
        self.save()
        print(f"문제 '{deleted_quiz['question']}' \n삭제되었습니다. 메뉴로 돌아갑니다.")

    def get_history(self):
        print("게임 기록을 조회합니다.")

        if not self.history:
            print("기록이 없습니다.")
            return

        for record in self.history[::-1]:
            timestamp = record["timestamp"]
            questions = record["questions"]
            score = record["score"]
            print(f"날짜: {timestamp}, 문제 수: {questions}, 점수: {score}")


    def _get_user_answer(self, msg="정답은 (1-4, 힌트: 5) : ") -> int:
        while True:
            try:
                raw = get_user_input(msg)
                val = int(raw)
                if val < 1 or val > self.HINT_OPTION:
                    print(f"1-{self.HINT_OPTION} 사이의 숫자를 입력해주세요. (힌트: {self.HINT_OPTION})")
                    continue
                return val
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")
                continue

game = QuizGame()