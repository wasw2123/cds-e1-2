

class Quiz:
    def __init__(self, question:str , choices: list[str], answer: int, hint: str):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint


    def display(self, number: int) -> None:
        print(f"-----------------------")
        print(f"[문제 {number}] {self.question}")
        print(f"***힌트를 확인하고 싶으면 5번을 입력하세요.***\n")
        for i, c in enumerate(self.choices, start=1):
            print(f"{i}. {c}")

    def check_answer(self, user_answer: int) -> bool:
        return user_answer == self.answer
    