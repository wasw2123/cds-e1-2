from service.data import DEFAULT_DATA, data_control
from service.quiz import Quiz



class Game:
    def play(data: dict) -> None:
        print("게임을 시작합니다.\n")

        quizzes = data["quizzes"]
        if not quizzes:
            print("퀴즈 데이터가 존재하지 않습니다. 데이터를 초기화합니다.")
            data_control.save_data(DEFAULT_DATA)
            return None
        
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

    def list(data):
        print("문제 리스트를 조회합니다.")
        
    def score(data):
        print("점수를 조회합니다.")

    def exit(data):
        print("게임을 종료합니다.")

        return False