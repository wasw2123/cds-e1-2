from service.data import data_control
from service.quiz import Quiz



class Game:
    def play(data: dict) -> None:
        print("게임을 시작합니다.\n")

        quizzes = data.get("quizzes")
        if not quizzes:
            data_control.quiz_data_reset(data)
            return
        
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


    def add(data):
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
        data["quizzes"].append(new_quiz)
        data_control.save_data(data)
        print("퀴즈를 추가하였습니다. 메뉴로 돌아갑니다.")



    def list(data):
        print("문제 리스트를 조회합니다.")
        print("---------------------")

        quizzes = data.get("quizzes")
        if not quizzes:
            data_control.quiz_data_reset(data)
            return

        for i, q in enumerate(quizzes, start=1):
            quiz = Quiz(q["question"], q["choices"], q["answer"])

            quiz.display(i)
            print(f"\n정답 : {q["answer"]}")

        print(f"\n총 문제 수 : {len(quizzes)}")
        
    def score(data):
        print("점수를 조회합니다.")

    def exit(data):
        data_control.save_data(data)
        print("현재 상태를 저장하고 게임을 종료합니다.")

        return False