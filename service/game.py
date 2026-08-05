from random import randint
from datetime import datetime

from service.data import data_control
from service.quiz import Quiz


class QuizGame:
    def __init__(self):
        self.data = data_control.load_data() or {}
        # 안전한 기본값 설정
        self.data.setdefault("quizzes", [])
        self.data.setdefault("best_score", 0)
        self.quizzes = self.data["quizzes"]
        self.best_score = self.data["best_score"]
        self.MENUS = {
            1: ("퀴즈 풀기", self.play),
            2: ("퀴즈 추가", self.add),
            3: ("퀴즈 목록", self.list),
            4: ("점수 확인", self.score),
            5: ("문제 삭제", self.delete),
            6: ("게임 기록 조회", self.history),
            0: ("종료", self.exit),
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

        quizzes = self.data.get("quizzes", [])
        if not quizzes:
            data_control.quiz_data_reset(self.data)
            # data가 갱신되었으므로 로컬 참조 동기화
            self.quizzes = self.data.get("quizzes", [])
            quizzes = self.quizzes
            if not quizzes:
                return

        print("몇 문제를 풀지 선택해주세요. (최대 10문제)")
        while True:
            try:
                raw = input("문제 수: ").strip()
                if raw == "":
                    print("입력이 비었습니다. 숫자를 입력해주세요.")
                    continue
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
        selected_indices = []
        for _ in range(question_count):
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
                quiz.display_hint()
                point = self.HINT_SCORE
                user_answer = self._get_user_answer()

            if quiz.check_answer(user_answer):
                score += point
                print(f"정답입니다. {point}점 획득")
            else:
                print(f"틀렸습니다. 정답은: {quiz.answer}번 {quiz.choices[quiz.answer-1]}")

        print(f"\n 최종 점수 : {score}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data.setdefault("history", []).append({
            "timestamp": timestamp,
            "questions": question_count,
            "score": score
        })

        best_score = self.data.get("best_score", 0)
        if best_score < score:
            self.data["best_score"] = score
            self.best_score = score
            print("최고 점수가 갱신됐습니다.")
        data_control.save_data(self.data)


    def add(self):
        print("문제를 추가합니다.")
        while True:
            question = input("문제를 입력하세요 : ").strip()
            if question == "":
                print("문제를 비워둘 수 없습니다. 다시 입력해주세요.")
            else:
                break

        choices = []
        choice_range = range(1, 5)
        for i in choice_range:
            while True:
                c = input(f"선택지 {i}번 : ").strip()
                if c == "":
                    print("선택지는 비워둘 수 없습니다. 다시 입력해주세요.")
                else:
                    choices.append(c)
                    break

        answer = 0
        while answer not in choice_range:
            try:
                raw = input("정답 번호(1-4) : ").strip()
                if raw == "":
                    print("입력이 비었습니다. 1-4 사이 숫자를 입력해주세요.")
                    continue
                answer = int(raw)
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

        quizzes = self.data.get("quizzes", [])
        if not quizzes:
            data_control.quiz_data_reset(self.data)
            self.quizzes = self.data.get("quizzes", [])
            quizzes = self.quizzes
            if not quizzes:
                return

        for i, q in enumerate(quizzes, start=1):
            quiz = Quiz(q["question"], q["choices"], q["answer"], q.get("hint", "힌트가 없습니다."))

            quiz.display(i)
            quiz.display_hint()
            print(f"\n정답 : {q['answer']}")

        print(f"\n총 문제 수 : {len(quizzes)}")
        
    def score(self):
        print(f"현재 최고 점수는 {self.best_score}입니다")

    def exit(self):
        data_control.save_data(self.data)
        print("현재 상태를 저장하고 게임을 종료합니다.")

        return False

    def delete(self):
        print("문제를 삭제합니다.")
        quizzes = self.data.get("quizzes", [])
        if not quizzes:
            data_control.quiz_data_reset(self.data)
            self.quizzes = self.data.get("quizzes", [])
            quizzes = self.quizzes
            if not quizzes:
                return

        for i, q in enumerate(quizzes, start=1):
            quiz = Quiz(q["question"], q["choices"], q["answer"], q.get("hint", "힌트가 없습니다."))
            quiz.display(i)
            quiz.display_hint()
            print(f"\n정답 : {q['answer']}")
            print("---------------------")

        while True:
            try:
                raw = input("삭제할 문제 번호를 입력하세요 (취소는 0번) : ").strip()
                if raw == "":
                    print("입력이 비었습니다. 숫자를 입력해주세요.")
                    continue
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
        data_control.save_data(self.data)
        print(f"문제 '{deleted_quiz['question']}' \n삭제되었습니다. 메뉴로 돌아갑니다.")

    def history(self):
        print("게임 기록을 조회합니다.")
        history = self.data.get("history", [])
        if not history:
            print("기록이 없습니다.")
            return

        for record in history[::-1]:
            timestamp = record["timestamp"]
            questions = record["questions"]
            score = record["score"]
            print(f"날짜: {timestamp}, 문제 수: {questions}, 점수: {score}")


    def _get_user_answer(self) -> int:
        # 1-4 정답, 5는 힌트 옵션으로 허용. 입력 검증 루프 추가
        while True:
            try:
                raw = input("정답은 : ").strip()
                if raw == "":
                    print("입력이 비었습니다. 숫자를 입력해주세요.")
                    continue
                val = int(raw)
                if val < 1 or val > self.HINT_OPTION:
                    print(f"1-{self.HINT_OPTION} 사이의 숫자를 입력해주세요. (힌트: {self.HINT_OPTION})")
                    continue
                return val
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")

game = QuizGame()