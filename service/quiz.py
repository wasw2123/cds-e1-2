

class Quiz:
    def __init__(self, question:str , choices: list[str], answer: int, hint: str):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint


    def display(self, number: int) -> None:
        print(f"-----------------------")
        print(f"[문제 {number}] {self.question}")
        for i, c in enumerate(self.choices, start=1):
            print(f"{i}. {c}")

    def display_hint(self) -> None:
        print(f"-----------------------")
        print(f"힌트 : {self.hint}")

    def check_answer(self, user_answer: int) -> bool:
        return user_answer == self.answer
    