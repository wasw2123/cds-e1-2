# 파이썬 & Git 스터디 가이드

이 문서는 이번 퀴즈 게임 미션을 끝낸 뒤 스스로 설명할 수 있어야 하는 내용을 정리한 학습 가이드입니다.

목표는 문법을 외우는 것이 아니라, 내가 만든 프로그램이 왜 이렇게 동작하는지 설명할 수 있게 되는 것입니다. 그래서 각 개념은 다음 순서로 정리했습니다.

- 개념: 무엇인가
- 왜 필요한가: 퀴즈 게임에서 어떤 문제를 해결하는가
- 코드 예시: 실제로 어떻게 쓰는가
- 설명 연습: 발표나 회고 때 말할 수 있는 문장

---

## 1. Python 기초

### 1. 변수

변수는 값을 저장해 두고 나중에 다시 사용하기 위해 붙이는 이름입니다.

예를 들어 퀴즈 게임에서는 점수, 문제 수, 사용자 입력값, 최고 점수 같은 값이 계속 필요합니다. 이런 값을 매번 직접 쓰면 코드가 복잡해지고 수정하기 어렵습니다. 그래서 `score`, `question_count`, `user_answer`, `best_score` 같은 이름을 붙여 관리합니다.

```python
score = 0
best_score = 80
user_name = "철수"

score = score + 10
print(score)
```

위 코드에서 `score`는 처음에 `0`을 저장하고, 정답을 맞히면 `10`을 더해서 다시 저장합니다. 변수는 한 번 값을 넣고 끝나는 것이 아니라, 프로그램 흐름에 따라 값이 바뀔 수 있습니다.

퀴즈 게임 예시:

```python
score = 0

if user_answer == answer:
    score += 10
```

`score += 10`은 `score = score + 10`과 같은 뜻입니다.

설명 연습:

> 변수는 데이터를 기억하기 위해 사용하는 이름입니다. 퀴즈 게임에서는 현재 점수나 최고 점수처럼 계속 바뀌고 다시 사용해야 하는 값을 변수에 저장합니다.

---

### 2. 자료형

자료형은 값의 종류입니다. Python은 값의 종류에 따라 할 수 있는 일이 다릅니다.

이번 미션에서 특히 중요한 자료형은 `int`, `str`, `bool`, `list`, `dict`입니다.

| 자료형 | 뜻 | 예시 | 퀴즈 게임에서의 사용 |
| --- | --- | --- | --- |
| `int` | 정수 | `1`, `80` | 메뉴 번호, 정답 번호, 점수 |
| `str` | 문자열 | `"퀴즈 풀기"` | 문제 문장, 선택지, 안내 메시지 |
| `bool` | 참/거짓 | `True`, `False` | 정답 여부 판단 |
| `list` | 여러 값을 순서대로 저장 | `["A", "B", "C"]` | 선택지 목록, 퀴즈 목록 |
| `dict` | 이름표와 값을 짝으로 저장 | `{"score": 80}` | state.json의 퀴즈 데이터 |

#### int

`int`는 정수입니다. 계산하거나 범위를 비교할 때 사용합니다.

```python
menu_number = 1
answer = 3
score = 90
```

사용자 입력은 처음에는 문자열입니다. 숫자로 비교하려면 `int()`로 변환해야 합니다.

```python
raw = input("정답 번호: ")
user_answer = int(raw)
```

주의할 점은 `"3"`과 `3`은 다르다는 것입니다.

```python
print("3" == 3)  # False
```

#### str

`str`은 문자열입니다. 글자 데이터를 표현합니다.

```python
question = "Python의 창시자는?"
message = "정답입니다."
```

문자열 앞뒤 공백을 제거할 때는 `strip()`을 사용합니다.

```python
menu = input("메뉴 선택: ").strip()
```

이번 미션의 공통 입력 조건에서 "입력 앞뒤 공백 제거 후 처리"가 있었기 때문에 `strip()`이 중요합니다.

#### bool

`bool`은 참 또는 거짓을 나타냅니다.

```python
is_correct = user_answer == answer
```

`user_answer == answer`의 결과는 `True` 또는 `False`입니다.

```python
if is_correct:
    print("정답입니다.")
else:
    print("틀렸습니다.")
```

#### list

`list`는 여러 값을 순서대로 담는 자료형입니다.

```python
choices = ["Guido", "Linus", "Bjarne", "James"]

print(choices[0])  # Guido
print(choices[1])  # Linus
```

Python 리스트의 인덱스는 0부터 시작합니다. 하지만 퀴즈 정답 번호는 사용자가 보기 쉽게 1부터 4까지 사용합니다.

그래서 정답 선택지를 출력할 때는 `enumerate(..., start=1)`을 사용하면 좋습니다.

```python
for number, choice in enumerate(choices, start=1):
    print(f"{number}. {choice}")
```

#### dict

`dict`는 key와 value를 짝으로 저장합니다.

```python
quiz_data = {
    "question": "Python의 창시자는?",
    "choices": ["Guido", "Linus", "Bjarne", "James"],
    "answer": 1,
    "hint": "네덜란드 출신입니다."
}

print(quiz_data["question"])
print(quiz_data["choices"])
```

설명 연습:

> 자료형은 데이터의 종류입니다. 점수나 정답 번호는 계산과 비교가 필요해서 int를 쓰고, 문제와 선택지는 글자이기 때문에 str을 씁니다. 여러 선택지는 list로 묶고, 문제 하나의 전체 정보는 dict로 저장합니다.

---

### 3. 조건문: if / elif / else

조건문은 상황에 따라 다른 코드를 실행하게 만드는 문법입니다.

퀴즈 게임에서는 다음과 같은 판단이 필요합니다.

- 사용자가 메뉴 1번을 골랐는가?
- 정답 번호가 1부터 4 사이인가?
- 사용자가 입력한 답이 실제 정답인가?
- 현재 점수가 최고 점수보다 높은가?
- 저장 파일이 존재하는가?

기본 구조:

```python
if 조건:
    조건이 참일 때 실행
elif 다른_조건:
    다른 조건이 참일 때 실행
else:
    위 조건이 모두 아닐 때 실행
```

퀴즈 정답 확인 예시:

```python
if user_answer == answer:
    print("정답입니다.")
else:
    print("틀렸습니다.")
```

메뉴 처리 예시:

```python
if menu_selected == 1:
    play()
elif menu_selected == 2:
    add_quiz()
elif menu_selected == 0:
    exit_game()
else:
    print("잘못된 메뉴입니다.")
```

범위 검사 예시:

```python
if answer < 1 or answer > 4:
    print("1부터 4 사이의 숫자를 입력해주세요.")
```

`or`는 둘 중 하나라도 참이면 전체가 참입니다. 위 코드는 `answer`가 1보다 작거나 4보다 크면 잘못된 입력으로 처리합니다.

설명 연습:

> 조건문은 프로그램이 상황에 따라 다른 동작을 하게 만드는 문법입니다. 퀴즈 게임에서는 메뉴 선택, 정답 여부, 입력 범위 검사, 최고 점수 갱신 같은 부분에서 조건문을 사용했습니다.

---

### 4. 반복문: for와 while

반복문은 같은 형태의 작업을 여러 번 실행할 때 사용합니다.

`for`와 `while`은 모두 반복문이지만 쓰임이 다릅니다.

| 구분 | 주로 쓰는 상황 | 퀴즈 게임 예시 |
| --- | --- | --- |
| `for` | 반복할 대상이나 횟수가 정해져 있을 때 | 퀴즈 목록 출력, 선택지 4개 출력 |
| `while` | 언제 끝날지 조건에 따라 결정될 때 | 올바른 입력을 받을 때까지 재입력 |

#### for

`for`는 리스트처럼 여러 개의 데이터가 있을 때 하나씩 꺼내며 반복합니다.

```python
choices = ["Guido", "Linus", "Bjarne", "James"]

for choice in choices:
    print(choice)
```

번호도 함께 출력하려면 `enumerate()`를 사용합니다.

```python
for number, choice in enumerate(choices, start=1):
    print(f"{number}. {choice}")
```

퀴즈 목록 출력에도 `for`가 적합합니다.

```python
for index, quiz in enumerate(quizzes, start=1):
    print(f"[{index}] {quiz['question']}")
```

#### while

`while`은 조건이 참인 동안 계속 반복합니다.

```python
while True:
    menu = input("메뉴 선택: ").strip()

    if menu == "0":
        break
```

`while True`는 무한 반복입니다. 하지만 `break`를 만나면 반복을 종료합니다.

입력 검증 예시:

```python
while True:
    raw = input("정답 번호: ").strip()

    if raw == "":
        print("입력이 비었습니다.")
        continue

    try:
        answer = int(raw)
    except ValueError:
        print("숫자를 입력해주세요.")
        continue

    if 1 <= answer <= 4:
        break

    print("1부터 4 사이의 숫자를 입력해주세요.")
```

`continue`는 아래 코드를 건너뛰고 다음 반복으로 돌아갑니다. 잘못된 입력을 받았을 때 재입력을 유도하기 좋습니다.

설명 연습:

> for는 퀴즈 목록이나 선택지처럼 반복할 대상이 정해져 있을 때 사용합니다. while은 사용자가 올바른 값을 입력할 때까지 계속 물어봐야 하는 상황처럼 반복 종료 시점이 입력에 따라 달라질 때 사용합니다.

---

### 5. 함수

함수는 특정 작업을 이름 붙여 분리한 코드 묶음입니다.

함수를 사용하는 이유는 다음과 같습니다.

- 같은 코드를 반복해서 쓰지 않아도 됩니다.
- 코드의 역할이 분명해집니다.
- 오류가 생겼을 때 고칠 위치를 찾기 쉽습니다.
- 큰 프로그램을 작은 기능 단위로 나눌 수 있습니다.

기본 구조:

```python
def 함수이름(매개변수):
    실행할 코드
    return 반환값
```

예시:

```python
def calculate_score(correct_count, total_count):
    score = correct_count / total_count * 100
    return score

result = calculate_score(4, 5)
print(result)
```

#### 매개변수와 반환값

매개변수는 함수에 전달하는 입력값입니다.

```python
def greet(name):
    print(f"{name}님 안녕하세요.")

greet("철수")
```

반환값은 함수가 작업을 끝낸 뒤 돌려주는 결과입니다.

```python
def is_correct(user_answer, answer):
    return user_answer == answer

result = is_correct(2, 2)
print(result)  # True
```

#### 이번 프로젝트의 함수 예시

`service/core.py`의 `get_user_input()`은 빈 입력을 막기 위한 공통 입력 함수입니다.

```python
def get_user_input(prompt: str, msg: str = "입력이 비었습니다. 다시 입력해주세요.") -> str:
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print(msg)
        else:
            return user_input
```

이 함수를 사용하면 문제 입력, 선택지 입력, 정답 입력에서 빈 문자열 검사를 반복해서 작성하지 않아도 됩니다.

설명 연습:

> 함수는 특정 기능을 재사용할 수 있게 묶어 둔 코드입니다. 이번 프로젝트에서는 입력 처리처럼 여러 곳에서 반복되는 로직을 함수로 분리해서 코드 중복을 줄였습니다.

---

## 2. 클래스와 객체

### 1. 클래스란 무엇인가

클래스는 관련 있는 데이터와 기능을 한곳에 묶어 둔 설계도입니다.

퀴즈 하나에는 다음 정보가 필요합니다.

- 문제 문장
- 선택지 4개
- 정답 번호
- 힌트

그리고 퀴즈 하나는 다음 동작도 할 수 있어야 합니다.

- 문제를 출력한다.
- 힌트를 출력한다.
- 사용자의 답이 맞는지 확인한다.

이처럼 데이터와 동작이 함께 다니는 경우 클래스가 잘 어울립니다.

```python
class Quiz:
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def check_answer(self, user_answer):
        return user_answer == self.answer
```

설명 연습:

> 클래스는 관련된 데이터와 기능을 묶는 설계도입니다. 퀴즈 게임에서는 문제, 선택지, 정답 같은 데이터를 Quiz 클래스로 묶고, 게임 진행과 저장은 QuizGame 클래스로 분리했습니다.

---

### 2. 객체란 무엇인가

객체는 클래스를 바탕으로 실제로 만들어진 값입니다.

클래스가 설계도라면 객체는 설계도로 만든 실제 제품입니다.

```python
quiz = Quiz(
    "Python의 창시자는?",
    ["Guido", "Linus", "Bjarne", "James"],
    1,
    "네덜란드 출신입니다."
)
```

위 코드에서 `Quiz`는 클래스이고, `quiz`는 객체입니다.

객체의 속성에 접근할 때는 점(`.`)을 사용합니다.

```python
print(quiz.question)
print(quiz.answer)
```

객체의 메서드도 점(`.`)으로 호출합니다.

```python
quiz.check_answer(1)
```

---

### 3. __init__ 메서드

`__init__`은 객체가 생성될 때 자동으로 실행되는 특별한 메서드입니다.

```python
class Quiz:
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint
```

`Quiz(...)`처럼 객체를 만들면 Python이 내부적으로 `__init__`을 호출합니다.

```python
quiz = Quiz("문제", ["A", "B", "C", "D"], 1, "힌트")
```

이때 전달한 값들이 `self.question`, `self.choices`, `self.answer`, `self.hint`에 저장됩니다.

설명 연습:

> __init__은 객체가 처음 만들어질 때 필요한 초기값을 넣어 주는 메서드입니다. Quiz 객체를 만들 때 문제, 선택지, 정답, 힌트를 받아서 객체 속성으로 저장합니다.

---

### 4. self의 역할

`self`는 객체 자기 자신을 가리킵니다.

```python
def check_answer(self, user_answer):
    return user_answer == self.answer
```

여기서 `self.answer`는 "이 퀴즈 객체가 가지고 있는 정답"이라는 뜻입니다.

예를 들어 서로 다른 퀴즈 객체가 있다면 각 객체는 자기만의 정답을 가집니다.

```python
quiz1 = Quiz("1번 문제", ["A", "B", "C", "D"], 1, "힌트1")
quiz2 = Quiz("2번 문제", ["A", "B", "C", "D"], 3, "힌트2")

print(quiz1.answer)  # 1
print(quiz2.answer)  # 3
```

`self`가 있기 때문에 같은 `check_answer()` 메서드를 사용해도 각 객체의 정답과 비교할 수 있습니다.

설명 연습:

> self는 현재 메서드를 호출한 객체 자신을 의미합니다. 같은 Quiz 클래스에서 만든 객체라도 문제와 정답은 각각 다르기 때문에, self를 통해 각 객체의 속성에 접근합니다.

---

### 5. 속성과 메서드

속성은 객체가 가지고 있는 데이터입니다.

```python
self.question
self.choices
self.answer
self.hint
```

메서드는 객체가 할 수 있는 동작입니다.

```python
def display(self, number):
    print(f"[문제 {number}] {self.question}")

def check_answer(self, user_answer):
    return user_answer == self.answer
```

이번 프로젝트의 클래스 역할:

| 클래스 | 역할 |
| --- | --- |
| `Quiz` | 퀴즈 하나의 데이터와 출력/정답 확인 담당 |
| `QuizGame` | 메뉴, 게임 진행, 추가, 삭제, 점수, 기록, 저장 흐름 담당 |
| `DataControl` | `state.json` 저장과 불러오기 담당 |

이렇게 나누면 코드가 한 파일이나 한 함수에 몰리지 않고, 각 클래스가 맡은 책임이 분명해집니다.

설명 연습:

> 속성은 객체가 가진 데이터이고, 메서드는 객체가 수행하는 기능입니다. Quiz의 속성은 question, choices, answer, hint이고, 메서드는 display, display_hint, check_answer입니다.

---

## 3. 파일 입출력과 JSON

### 1. 파일 입출력이 필요한 이유

프로그램 안의 변수는 프로그램이 종료되면 사라집니다.

예를 들어 퀴즈를 추가한 뒤 프로그램을 종료하면, 그 데이터가 변수에만 있었다면 다음 실행 때 사라집니다. 추가한 퀴즈와 최고 점수를 유지하려면 파일에 저장해야 합니다.

이번 프로젝트에서는 프로젝트 루트의 `state.json` 파일에 데이터를 저장합니다.

저장하는 데이터 예시:

```json
{
    "quizzes": [
        {
            "question": "Python의 창시자는?",
            "choices": ["Guido", "Linus", "Bjarne", "James"],
            "answer": 1,
            "hint": "네덜란드 출신입니다."
        }
    ],
    "best_score": 80,
    "history": []
}
```

---

### 2. 파일 열기, 읽기, 쓰기

Python에서 파일을 다룰 때는 `open()`을 사용합니다.

쓰기:

```python
with open("state.json", "w", encoding="utf-8") as f:
    f.write("hello")
```

읽기:

```python
with open("state.json", "r", encoding="utf-8") as f:
    content = f.read()
```

`with`를 사용하면 파일을 사용한 뒤 자동으로 닫아 줍니다. 파일을 닫지 않으면 데이터가 제대로 저장되지 않거나 다른 프로그램에서 파일을 사용할 때 문제가 생길 수 있습니다.

`encoding="utf-8"`은 한글이 깨지지 않도록 하기 위해 중요합니다.

설명 연습:

> 파일 입출력은 프로그램 밖의 파일에 데이터를 저장하거나 불러오는 작업입니다. 이번 프로젝트에서는 프로그램을 종료해도 퀴즈와 최고 점수가 유지되도록 state.json을 읽고 씁니다.

---

### 3. JSON이란 무엇인가

JSON은 데이터를 저장하고 주고받기 위한 텍스트 형식입니다.

Python의 `dict`, `list`, `str`, `int`, `bool`과 구조가 비슷해서 퀴즈 데이터를 저장하기 좋습니다.

Python 데이터:

```python
data = {
    "best_score": 80,
    "quizzes": [
        {
            "question": "Python의 창시자는?",
            "choices": ["Guido", "Linus", "Bjarne", "James"],
            "answer": 1
        }
    ]
}
```

JSON 파일:

```json
{
    "best_score": 80,
    "quizzes": [
        {
            "question": "Python의 창시자는?",
            "choices": ["Guido", "Linus", "Bjarne", "James"],
            "answer": 1
        }
    ]
}
```

Python에서 JSON을 다룰 때는 표준 라이브러리 `json`을 사용합니다.

```python
import json
```

파일에 저장:

```python
with open("state.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

파일에서 불러오기:

```python
with open("state.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

`ensure_ascii=False`를 사용하면 한글이 `\uD55C\uAE00` 같은 형태로 변환되지 않고 그대로 저장됩니다.

`indent=4`는 사람이 읽기 좋게 들여쓰기해서 저장한다는 뜻입니다.

설명 연습:

> JSON은 데이터를 저장하기 위한 텍스트 형식입니다. Python의 dict와 list 구조와 비슷해서 퀴즈 목록, 최고 점수, 플레이 기록을 저장하기에 적합합니다.

---

### 4. try / except 예외 처리

예외 처리는 프로그램 실행 중 문제가 생겼을 때 비정상 종료되지 않도록 처리하는 문법입니다.

이번 미션에서 처리해야 하는 대표 예외:

- 숫자를 입력해야 하는데 `abc`를 입력한 경우
- 파일이 없는 경우
- `state.json` 파일이 손상된 경우
- 저장 중 오류가 발생한 경우
- 사용자가 Ctrl+C를 누른 경우
- 입력 스트림이 종료된 경우

기본 구조:

```python
try:
    문제가 생길 수 있는 코드
except 예외종류:
    문제가 생겼을 때 실행할 코드
```

숫자 입력 예시:

```python
try:
    user_answer = int(input("정답 번호: ").strip())
except ValueError:
    print("숫자를 입력해주세요.")
```

`int("abc")`는 숫자로 바꿀 수 없기 때문에 `ValueError`가 발생합니다.

파일 읽기 예시:

```python
try:
    with open("state.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("저장 파일이 없어 기본 데이터로 시작합니다.")
except json.JSONDecodeError:
    print("저장 파일이 손상되어 기본 데이터로 복구합니다.")
```

설명 연습:

> try/except는 오류가 발생할 수 있는 코드를 안전하게 실행하기 위한 문법입니다. 숫자 변환 실패나 state.json 손상처럼 예상 가능한 문제를 처리해서 프로그램이 갑자기 종료되지 않도록 합니다.

---

### 5. 데이터 파일 손상 처리

`state.json`은 사용자가 직접 열어 수정할 수도 있고, 저장 중 문제가 생기면 깨질 수도 있습니다.

예를 들어 JSON은 쉼표 하나가 잘못되어도 읽을 수 없습니다.

잘못된 JSON 예시:

```json
{
    "best_score": 80,
}
```

마지막 쉼표 때문에 `json.load()`가 실패할 수 있습니다.

이런 경우 프로그램이 바로 종료되면 사용자가 게임을 실행할 수 없습니다. 그래서 기본 데이터를 사용해 복구해야 합니다.

이번 프로젝트의 흐름:

1. `state.json`을 읽는다.
2. 파일이 없으면 기본 데이터로 시작하고 파일을 만든다.
3. JSON이 손상되었으면 안내 메시지를 출력한다.
4. 손상된 파일을 백업하거나 기본 데이터로 초기화한다.
5. 프로그램은 계속 실행된다.

설명 연습:

> 데이터 파일이 없거나 손상되어도 프로그램이 실행되어야 합니다. 그래서 FileNotFoundError와 JSONDecodeError를 처리하고, 문제가 있으면 기본 퀴즈 데이터로 복구하도록 만들었습니다.

---

## 4. Git 기초

### 1. Git이란 무엇인가

Git은 파일의 변경 이력을 기록하는 버전 관리 도구입니다.

프로그래밍을 하다 보면 다음 상황이 자주 생깁니다.

- 이전에 잘 되던 코드로 돌아가고 싶다.
- 어떤 기능을 언제 추가했는지 확인하고 싶다.
- 실험용 작업을 main 코드와 분리하고 싶다.
- GitHub에 올려 다른 컴퓨터에서도 코드를 받고 싶다.

Git은 이런 문제를 해결하기 위해 사용합니다.

설명 연습:

> Git은 코드의 변경 이력을 저장하고 관리하는 도구입니다. 기능 단위로 커밋하면 어떤 변경을 언제 왜 했는지 추적할 수 있고, 문제가 생겼을 때 이전 상태와 비교할 수 있습니다.

---

### 2. 저장소 초기화: git init

`git init`은 현재 폴더를 Git 저장소로 만드는 명령어입니다.

```bash
git init
```

실행하면 `.git` 폴더가 생기고, Git이 이 프로젝트의 변경 사항을 추적할 수 있게 됩니다.

주의할 점:

- `git init`만 했다고 모든 파일이 자동으로 저장되는 것은 아닙니다.
- 변경 내용을 기록하려면 `git add`와 `git commit`이 필요합니다.

설명 연습:

> git init은 현재 프로젝트 폴더를 Git이 관리하는 저장소로 초기화하는 명령입니다.

---

### 3. 변경 파일 확인: git status

`git status`는 현재 어떤 파일이 변경되었는지, 어떤 파일이 커밋 대기 상태인지 보여 줍니다.

```bash
git status
```

자주 확인해야 하는 이유:

- 실수로 원하지 않는 파일을 커밋하는 것을 막을 수 있습니다.
- 어떤 파일을 아직 `git add`하지 않았는지 알 수 있습니다.
- 현재 브랜치가 무엇인지 확인할 수 있습니다.

설명 연습:

> git status는 현재 작업 디렉터리의 변경 상태를 확인하는 명령입니다. 커밋하기 전에 어떤 파일이 포함될지 확인할 때 사용합니다.

---

### 4. 스테이징: git add

`git add`는 커밋에 포함할 파일을 고르는 명령어입니다.

```bash
git add main.py
git add README.md
```

모든 변경 파일을 한 번에 추가할 수도 있습니다.

```bash
git add .
```

하지만 처음에는 파일을 직접 지정하는 습관이 좋습니다. 그래야 원하지 않는 파일이 커밋에 들어가는 실수를 줄일 수 있습니다.

설명 연습:

> git add는 변경된 파일 중 이번 커밋에 포함할 파일을 스테이징 영역에 올리는 명령입니다.

---

### 5. 커밋: git commit

`git commit`은 스테이징된 변경 내용을 하나의 기록으로 저장합니다.

```bash
git commit -m "Feat: 메뉴 기능 구현"
```

커밋은 기능 단위로 나누는 것이 좋습니다.

좋은 커밋 예시:

```bash
git commit -m "Feat: Quiz 클래스 추가"
git commit -m "Feat: 퀴즈 추가 기능 구현"
git commit -m "Fix: 잘못된 정답 입력 처리"
git commit -m "Docs: README 실행 방법 추가"
```

나쁜 커밋 예시:

```bash
git commit -m "수정"
git commit -m "작업"
git commit -m "asdf"
```

왜냐하면 나중에 `git log`를 봤을 때 무엇을 바꿨는지 알기 어렵기 때문입니다.

설명 연습:

> git commit은 선택한 변경 사항을 하나의 이력으로 저장하는 명령입니다. 기능 단위로 커밋하면 개발 과정을 설명하기 쉽고, 문제가 생겼을 때 원인을 찾기 쉽습니다.

---

### 6. 브랜치와 checkout

브랜치는 작업 흐름을 분리하기 위한 가지입니다.

예를 들어 `main` 브랜치에는 안정적인 코드를 두고, `feature/play-quiz` 브랜치에서 퀴즈 풀기 기능을 만들 수 있습니다.

브랜치 생성과 이동:

```bash
git checkout -b feature/play-quiz
```

기존 브랜치로 이동:

```bash
git checkout main
```

브랜치를 쓰는 이유:

- main 코드를 바로 망가뜨리지 않고 새 기능을 만들 수 있습니다.
- 기능별 작업 기록이 분리됩니다.
- 나중에 팀 프로젝트에서 Pull Request 흐름으로 확장할 수 있습니다.

설명 연습:

> 브랜치는 main 코드와 분리해서 새 기능을 개발하기 위한 작업 공간입니다. checkout은 브랜치를 이동하거나 새 브랜치를 만들어 이동할 때 사용합니다.

---

### 7. 병합: git merge

`git merge`는 다른 브랜치에서 작업한 내용을 현재 브랜치로 합치는 명령입니다.

예시 흐름:

```bash
git checkout -b feature/play-quiz
# 퀴즈 풀기 기능 작업
git add service/game.py
git commit -m "Feat: 퀴즈 풀기 기능 구현"

git checkout main
git merge feature/play-quiz
```

위 흐름은 다음 뜻입니다.

1. `feature/play-quiz` 브랜치에서 기능을 만든다.
2. 기능 완성 후 커밋한다.
3. `main`으로 돌아온다.
4. `feature/play-quiz`의 변경사항을 `main`에 합친다.

설명 연습:

> merge는 한 브랜치의 변경사항을 다른 브랜치에 합치는 명령입니다. 이번 미션에서는 퀴즈 풀기 기능을 별도 브랜치에서 만든 뒤 main으로 병합하는 흐름을 경험합니다.

---

### 8. 원격 저장소와 push

GitHub 저장소는 원격 저장소입니다. 로컬 컴퓨터의 Git 저장소를 GitHub에 연결하면 코드를 온라인에 올릴 수 있습니다.

원격 저장소 확인:

```bash
git remote -v
```

원격 저장소 추가:

```bash
git remote add origin https://github.com/사용자명/저장소명.git
```

GitHub로 업로드:

```bash
git push origin main
```

`origin`은 원격 저장소의 기본 이름이고, `main`은 올릴 브랜치 이름입니다.

설명 연습:

> push는 로컬 Git 커밋을 GitHub 같은 원격 저장소에 업로드하는 명령입니다.

---

### 9. clone

`git clone`은 GitHub에 있는 저장소를 내 컴퓨터의 새 폴더로 복제하는 명령입니다.

```bash
git clone https://github.com/사용자명/저장소명.git
```

이번 미션에서 clone을 하는 이유는 원격 저장소를 다른 위치에서 새로 받아 보는 경험을 하기 위해서입니다.

실습 흐름:

```bash
cd ..
git clone https://github.com/사용자명/저장소명.git mission2-clone
cd mission2-clone
```

설명 연습:

> clone은 원격 저장소의 전체 프로젝트와 Git 이력을 새로운 로컬 폴더로 복제하는 명령입니다.

---

### 10. pull

`git pull`은 원격 저장소의 최신 변경사항을 현재 로컬 저장소로 가져와 합치는 명령입니다.

```bash
git pull origin main
```

이번 미션의 clone/pull 실습 흐름:

1. 기존 프로젝트를 GitHub에 push한다.
2. 다른 폴더에 `git clone`한다.
3. clone한 폴더에서 README를 조금 수정한다.
4. commit 후 push한다.
5. 원래 작업 폴더로 돌아온다.
6. `git pull origin main`으로 변경사항을 가져온다.

설명 연습:

> pull은 원격 저장소에 새로 올라온 커밋을 내 로컬 저장소로 가져오는 명령입니다. 다른 위치나 다른 사람이 올린 변경사항을 현재 프로젝트에 반영할 때 사용합니다.

---

## 5. 이번 프로젝트 코드 흐름 이해

### 1. 실행 흐름

프로그램은 `main.py`에서 시작합니다.

```python
from service.run_game import run

if __name__ == "__main__":
    run()
```

`if __name__ == "__main__":`는 이 파일을 직접 실행했을 때만 `run()`을 호출하겠다는 뜻입니다.

실행 흐름을 말로 정리하면 다음과 같습니다.

1. 사용자가 `python main.py`를 실행한다.
2. `main.py`가 `run()` 함수를 호출한다.
3. `run()`이 `QuizGame` 객체를 실행한다.
4. `QuizGame`은 저장된 데이터를 불러온다.
5. 메뉴를 보여 주고 사용자 입력에 따라 기능을 실행한다.
6. 퀴즈 추가, 점수 갱신, 기록 변경이 있으면 `state.json`에 저장한다.

---

### 2. Quiz 클래스 흐름

`Quiz` 클래스는 퀴즈 한 문제를 표현합니다.

주요 속성:

- `question`: 문제 문장
- `choices`: 선택지 목록
- `answer`: 정답 번호
- `hint`: 힌트

주요 메서드:

- `display()`: 문제와 선택지를 출력
- `display_hint()`: 힌트를 출력
- `check_answer()`: 사용자의 답과 정답을 비교

역할 설명:

> Quiz 클래스는 문제 하나의 데이터와 동작을 담당합니다. 게임 전체 흐름은 알 필요가 없고, 자신이 가진 문제를 출력하고 정답을 확인하는 역할만 합니다.

---

### 3. QuizGame 클래스 흐름

`QuizGame` 클래스는 게임 전체를 관리합니다.

주요 속성:

- `quizzes`: 퀴즈 목록
- `best_score`: 최고 점수
- `history`: 플레이 기록
- `MENUS`: 메뉴 번호와 실행할 메서드 연결

주요 메서드:

- `menu()`: 메뉴 출력과 선택 처리
- `play()`: 퀴즈 풀기
- `add()`: 퀴즈 추가
- `list()`: 퀴즈 목록 조회
- `score()`: 최고 점수 조회
- `delete()`: 퀴즈 삭제
- `get_history()`: 게임 기록 조회
- `save()`: 현재 상태 저장
- `_get_user_answer()`: 정답 입력 처리

역할 설명:

> QuizGame은 게임 진행을 총괄하는 클래스입니다. 메뉴에서 어떤 기능을 실행할지 결정하고, 퀴즈 목록과 점수 상태를 관리하며, 변경사항을 저장합니다.

---

### 4. DataControl 클래스 흐름

`DataControl`은 데이터 저장과 불러오기를 담당합니다.

주요 역할:

- `state.json` 경로 관리
- UTF-8 인코딩으로 파일 읽기/쓰기
- JSON 저장과 불러오기
- 파일이 없을 때 기본 데이터 생성
- 파일이 손상되었을 때 기본 데이터로 복구

역할 설명:

> DataControl은 파일 입출력 책임을 분리한 클래스입니다. QuizGame이 게임 흐름에 집중할 수 있도록 저장과 불러오기 로직을 따로 담당합니다.

---

## 6. 입력 처리 기준 정리

이번 미션에서는 잘못된 입력을 처리하는 것이 중요합니다.

처리해야 하는 입력:

- `" 1 "`처럼 앞뒤 공백이 있는 입력
- `"abc"`처럼 숫자로 바꿀 수 없는 입력
- `""`처럼 빈 입력
- 메뉴 범위를 벗어난 숫자
- 정답 범위를 벗어난 숫자
- Ctrl+C
- EOF

기본 처리 패턴:

```python
while True:
    try:
        raw = input("선택: ").strip()

        if raw == "":
            print("입력이 비었습니다.")
            continue

        selected = int(raw)

        if selected < 1 or selected > 5:
            print("허용 범위 밖의 숫자입니다.")
            continue

        break

    except ValueError:
        print("숫자를 입력해주세요.")
    except (KeyboardInterrupt, EOFError):
        print("입력이 중단되었습니다. 저장 후 종료합니다.")
        break
```

핵심은 사용자의 실수를 프로그램 오류로 취급하지 않는 것입니다. 사용자가 잘못 입력하면 안내 메시지를 보여 주고 다시 입력받아야 합니다.

설명 연습:

> 사용자 입력은 항상 예상과 다를 수 있기 때문에 검증이 필요합니다. strip으로 공백을 제거하고, 빈 입력과 숫자 변환 실패, 범위 초과를 처리해서 프로그램이 안정적으로 동작하도록 했습니다.

---

## 7. 발표 또는 README에 쓸 수 있는 요약 문장

Python 기초:

> 이 프로젝트에서는 변수로 점수와 사용자 입력을 저장하고, int, str, list, dict 같은 자료형을 사용해 퀴즈 데이터를 표현했습니다. 조건문으로 메뉴 선택과 정답 여부를 판단하고, 반복문으로 메뉴를 계속 보여 주거나 퀴즈 목록을 순회했습니다.

클래스:

> Quiz 클래스는 퀴즈 한 문제의 데이터와 정답 확인 기능을 담당하고, QuizGame 클래스는 메뉴와 게임 진행, 점수 관리, 저장 흐름을 담당합니다. 클래스를 나누어 각 코드의 책임을 분리했습니다.

파일 입출력:

> 추가한 퀴즈와 최고 점수가 프로그램 종료 후에도 유지되도록 state.json 파일에 저장했습니다. json.dump로 저장하고 json.load로 불러오며, 파일이 없거나 손상된 경우에는 기본 데이터로 복구하도록 예외 처리를 했습니다.

Git:

> Git으로 기능 단위 커밋을 만들고, 브랜치를 생성해 퀴즈 풀기 기능을 작업한 뒤 main 브랜치에 병합했습니다. GitHub 원격 저장소에 push하고, clone과 pull을 통해 원격 저장소의 변경사항을 가져오는 흐름도 실습했습니다.

---

## 8. 최종 점검 체크리스트

아래 질문에 답할 수 있으면 미션 목표를 잘 이해한 것입니다.

Python:

- 변수는 왜 필요한가?
- `int`, `str`, `bool`, `list`, `dict`는 각각 언제 사용하는가?
- `if / elif / else`는 어떤 상황에서 쓰는가?
- `for`와 `while`의 차이는 무엇인가?
- 함수의 매개변수와 반환값은 무엇인가?

클래스:

- 클래스와 객체의 차이는 무엇인가?
- `__init__`은 언제 실행되는가?
- `self`는 무엇을 가리키는가?
- 속성과 메서드의 차이는 무엇인가?
- `Quiz`와 `QuizGame`은 각각 어떤 책임을 가지는가?

파일 입출력:

- 프로그램이 종료되면 변수 값은 어떻게 되는가?
- `state.json`은 왜 필요한가?
- JSON은 어떤 구조를 가지는가?
- `json.dump()`와 `json.load()`의 차이는 무엇인가?
- `try/except`는 왜 필요한가?

Git:

- `git init`은 무엇을 하는가?
- `git add`와 `git commit`의 차이는 무엇인가?
- 브랜치는 왜 사용하는가?
- `checkout`과 `merge`는 무엇을 하는가?
- `push`, `clone`, `pull`은 각각 언제 사용하는가?

---

## 9. 자주 헷갈리는 부분

### "3"과 3은 다르다

```python
print("3" == 3)  # False
```

`input()`으로 받은 값은 문자열입니다. 숫자 비교를 하려면 `int()` 변환이 필요합니다.

---

### 리스트 인덱스는 0부터, 정답 번호는 1부터

```python
choices = ["A", "B", "C", "D"]

print(choices[0])  # 1번 선택지
print(choices[1])  # 2번 선택지
```

사용자는 1번부터 보기 때문에 출력할 때는 `enumerate(..., start=1)`을 사용하면 좋습니다.

---

### return과 print는 다르다

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

`return`은 함수 밖으로 값을 돌려주는 것이고, `print`는 화면에 출력하는 것입니다.

---

### git add는 저장이 아니라 커밋 준비다

```bash
git add main.py
git commit -m "Feat: 메뉴 기능 구현"
```

`git add`는 커밋에 포함할 파일을 고르는 단계이고, 실제 이력 저장은 `git commit`에서 이루어집니다.

---

### JSON 파일은 문법이 엄격하다

잘못된 예:

```json
{
    "score": 80,
}
```

마지막 쉼표 때문에 오류가 날 수 있습니다. 그래서 `state.json`은 직접 수정하기보다 프로그램을 통해 저장하는 것이 안전합니다.
