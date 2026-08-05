def get_user_input(prompt: str, msg: str = "입력이 비었습니다. 다시 입력해주세요.") -> str:
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print(msg)
        else:
            return user_input