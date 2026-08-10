# 파이썬 & Git 스터디 가이드

이 문서는 이번 퀴즈 게임 미션을 끝낸 뒤 스스로 설명할 수 있어야 하는 내용을 정리한 학습 가이드입니다.

목표는 문법을 외우는 것이 아니라, 내가 만든 프로그램이 왜 이렇게 동작하는지 설명할 수 있게 되는 것입니다. 그래서 각 개념은 다음 순서로 정리했습니다.

- 개념: 무엇인가
- 왜 필요한가: 퀴즈 게임에서 어떤 문제를 해결하는가
- 코드 예시: 실제로 어떻게 쓰는가
- 요약: 앞에서 배운 내용을 짧게 정리한 문장

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

요약:

> 변수는 데이터를 기억하기 위해 사용하는 이름입니다. 퀴즈 게임에서는 현재 점수나 최고 점수처럼 계속 바뀌고 다시 사용해야 하는 값을 변수에 저장합니다.

---

### 2. 자료형과 자주 쓰는 기능

자료형은 값의 종류입니다. Python은 값의 종류에 따라 할 수 있는 일과 사용할 수 있는 메서드가 달라집니다.

이번 미션에서 특히 중요한 자료형은 `int`, `str`, `bool`, `list`, `dict`입니다. 함께 알아 두면 좋은 `float`, `tuple`, `set`, `None`도 뒤에서 간단히 다룹니다.

| 자료형 | 뜻 | 예시 | 퀴즈 게임에서의 사용 |
| --- | --- | --- | --- |
| `int` | 정수 | `1`, `80`, `-3` | 메뉴 번호, 정답 번호, 점수 |
| `float` | 소수점이 있는 수 | `3.14`, `80.5` | 평균이나 비율 계산 |
| `str` | 문자열 | `"퀴즈 풀기"` | 문제 문장, 선택지, 안내 메시지 |
| `bool` | 참/거짓 | `True`, `False` | 정답 여부 판단 |
| `list` | 여러 값을 순서대로 저장 | `["A", "B", "C"]` | 선택지 목록, 퀴즈 목록 |
| `tuple` | 수정할 수 없는 순서 있는 묶음 | `(10, 20)` | 바뀌면 안 되는 값 묶음 |
| `dict` | 키와 값을 짝으로 저장 | `{"score": 80}` | 퀴즈 한 문제의 전체 정보 |
| `set` | 중복 없는 값의 모음 | `{"A", "B"}` | 중복 제거, 포함 여부 확인 |
| `None` | 값이 없음을 나타내는 특별한 값 | `None` | 아직 결과가 없거나 반환값이 없음 |

자료형은 `type()`으로 확인할 수 있습니다.

```python
print(type(3))          # <class 'int'>
print(type("3"))        # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
```

`isinstance()`는 어떤 값이 특정 자료형인지 `True` 또는 `False`로 알려 줍니다.

```python
answer = 3

print(isinstance(answer, int))  # True
print(isinstance(answer, str))  # False
```

#### int와 float

`int`는 정수이고 `float`는 소수점이 있는 수입니다.

```python
menu_number = 1
score = 90
average = 8.5
```

숫자에는 다음과 같은 연산을 자주 사용합니다.

```python
print(7 + 2)   # 9: 더하기
print(7 - 2)   # 5: 빼기
print(7 * 2)   # 14: 곱하기
print(7 / 2)   # 3.5: 나누기 결과는 float
print(7 // 2)  # 3: 몫
print(7 % 2)   # 1: 나머지
print(2 ** 3)  # 8: 거듭제곱
```

사용자 입력은 처음에는 문자열입니다. 숫자로 계산하거나 비교하려면 `int()` 또는 `float()`로 변환해야 합니다.

```python
raw = input("정답 번호: ")
user_answer = int(raw)
```

주의할 점은 `"3"`과 `3`은 다르다는 것입니다.

```python
print("3" == 3)  # False
```

`int("abc")`처럼 숫자가 아닌 문자열을 변환하면 `ValueError`가 발생하므로 사용자 입력은 `try/except`로 처리하는 것이 안전합니다.

#### str

`str`은 글자 데이터를 나타내는 문자열입니다. 따옴표로 만듭니다.

```python
question = "Python의 창시자는?"
message = '정답입니다.'
```

문자열도 리스트처럼 순서가 있어서 인덱스와 슬라이싱을 사용할 수 있습니다.

```python
word = "Python"

print(word[0])    # P
print(word[-1])   # n: 뒤에서 첫 번째
print(word[0:3])  # Pyt: 0번부터 3번 직전까지
print(len(word))  # 6
```

자주 사용하는 문자열 메서드:

| 메서드 | 의미 | 예시 결과 |
| --- | --- | --- |
| `strip()` | 앞뒤 공백 제거 | `"  1  ".strip()` → `"1"` |
| `lower()` | 영어를 소문자로 변환 | `"YES".lower()` → `"yes"` |
| `upper()` | 영어를 대문자로 변환 | `"yes".upper()` → `"YES"` |
| `replace(a, b)` | 문자열 일부를 교체 | `"A-B".replace("-", ":")` → `"A:B"` |
| `split(기준)` | 문자열을 나누어 리스트로 반환 | `"A,B".split(",")` → `["A", "B"]` |
| `구분자.join(목록)` | 문자열 목록을 하나로 연결 | `", ".join(["A", "B"])` → `"A, B"` |

이번 미션에서는 입력 앞뒤 공백을 제거하기 위해 `strip()`을 자주 사용합니다.

```python
menu = input("메뉴 선택: ").strip()
```

문자열은 한 번 만들어지면 그 내용 자체를 바꿀 수 없습니다. `strip()`이나 `replace()`는 원본을 수정하지 않고 새로운 문자열을 돌려줍니다.

```python
raw = "  1  "
cleaned = raw.strip()

print(raw)      # "  1  " 그대로
print(cleaned)  # "1"
```

#### bool과 참처럼/거짓처럼 판단되는 값

`bool`은 참 또는 거짓을 나타내며 값은 `True`, `False` 두 개입니다.

```python
is_correct = user_answer == answer
print(is_correct)  # 비교 결과에 따라 True 또는 False
```

조건문에는 꼭 `True`나 `False`만 넣을 필요가 없습니다. Python은 다른 값도 참 또는 거짓처럼 판단합니다. 이를 보통 **Truthy(참 같은 값)**, **Falsy(거짓 같은 값)**라고 부릅니다.

대표적인 Falsy 값:

| 값 | 의미 |
| --- | --- |
| `False` | 거짓 자체 |
| `None` | 값이 없음 |
| `0`, `0.0` | 숫자 0 |
| `""` | 빈 문자열 |
| `[]` | 빈 리스트 |
| `{}` | 빈 딕셔너리 |
| `()` | 빈 튜플 |
| `set()` | 빈 세트 |

```python
print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool({}))      # False

print(bool(1))       # True
print(bool("hello")) # True
print(bool([0]))     # True: 안에 0이 있어도 리스트 자체는 비어 있지 않음
```

문자열 `"False"`와 `"0"`도 비어 있지 않은 문자열이므로 `True`처럼 판단된다는 점에 주의합니다.

```python
print(bool("False"))  # True
print(bool("0"))      # True
```

이 성질을 이용하면 목록이나 입력이 비었는지 간단히 확인할 수 있습니다.

```python
if not quizzes:
    print("퀴즈가 없습니다.")

if user_input:
    print("무언가 입력했습니다.")
```

`not`은 참과 거짓을 반대로 바꿉니다. 따라서 `not []`는 `True`이고 `not [1]`은 `False`입니다.

#### list

`list`는 여러 값을 순서대로 담는 자료형입니다. 요소를 추가·수정·삭제할 수 있는 **변경 가능한(mutable)** 자료형입니다.

```python
choices = ["Guido", "Linus", "Bjarne", "James"]

print(choices[0])   # Guido
print(choices[-1])  # James
print(choices[1:3]) # ["Linus", "Bjarne"]
print(len(choices)) # 4
```

Python 리스트의 인덱스는 0부터 시작합니다. 하지만 퀴즈 정답 번호는 사용자가 보기 쉽게 1부터 4까지 사용합니다.

```python
for number, choice in enumerate(choices, start=1):
    print(f"{number}. {choice}")
```

자주 사용하는 리스트 메서드:

| 메서드 | 의미 | 예시 |
| --- | --- | --- |
| `append(x)` | 맨 뒤에 요소 하나 추가 | `choices.append("Dennis")` |
| `extend(목록)` | 여러 요소를 맨 뒤에 추가 | `choices.extend(["A", "B"])` |
| `insert(i, x)` | 원하는 인덱스에 요소 추가 | `choices.insert(0, "첫 선택지")` |
| `remove(x)` | 값과 같은 첫 요소 삭제 | `choices.remove("Linus")` |
| `pop(i)` | 해당 인덱스의 요소를 꺼내며 삭제 | `deleted = choices.pop(1)` |
| `clear()` | 모든 요소 삭제 | `choices.clear()` |
| `index(x)` | 값이 처음 나온 인덱스 반환 | `choices.index("Guido")` |
| `count(x)` | 같은 값의 개수 반환 | `choices.count("Guido")` |
| `sort()` | 원본 리스트를 오름차순 정렬 | `scores.sort()` |
| `reverse()` | 원본 리스트의 순서를 뒤집음 | `choices.reverse()` |
| `copy()` | 얕은 복사본 생성 | `copied = choices.copy()` |

`append()`는 전달한 값 하나를 그대로 넣고, `extend()`는 전달한 목록 안의 요소를 하나씩 넣습니다.

```python
items = [1, 2]
items.append([3, 4])
print(items)  # [1, 2, [3, 4]]

items = [1, 2]
items.extend([3, 4])
print(items)  # [1, 2, 3, 4]
```

리스트에 값이 있는지는 `in`으로 확인합니다.

```python
if "Guido" in choices:
    print("선택지에 있습니다.")
```

`append()`와 `sort()`는 원본 리스트를 직접 바꾸고 `None`을 반환합니다. 다음처럼 작성하면 `scores`에 정렬된 리스트가 아니라 `None`이 저장됩니다. 반면 `pop()`은 원본에서 요소를 삭제하면서 그 요소를 반환합니다.

```python
scores = [30, 10, 20]
scores.sort()
print(scores)  # [10, 20, 30]

# 잘못 사용하기 쉬운 예
scores = scores.sort()
print(scores)  # None
```

#### dict

`dict`는 **key(키)**와 **value(값)**를 한 쌍으로 저장합니다. 리스트가 위치 번호로 값을 찾는다면 딕셔너리는 의미 있는 키로 값을 찾습니다. 키는 중복될 수 없고, 같은 키에 값을 다시 넣으면 기존 값이 바뀝니다.

```python
quiz_data = {
    "question": "Python의 창시자는?",
    "choices": ["Guido", "Linus", "Bjarne", "James"],
    "answer": 1,
    "hint": "네덜란드 출신입니다."
}
```

값 조회와 추가·수정:

```python
print(quiz_data["question"])  # 기존 키의 값 조회

quiz_data["score"] = 10       # 새 키와 값 추가
quiz_data["answer"] = 2       # 기존 키의 값 수정
```

`dict[키]`로 없는 키를 조회하면 `KeyError`가 발생합니다. 키가 없을 수도 있다면 `get()`을 사용합니다.

```python
print(quiz_data.get("hint"))                 # 있으면 힌트 반환
print(quiz_data.get("category"))             # 없으면 None 반환
print(quiz_data.get("wrong_count", 0))       # 없으면 기본값 0 반환
```

`get()`은 기본값을 돌려주기만 하고 딕셔너리에 새 키를 추가하지는 않습니다.

```python
data = {}
count = data.get("count", 0)

print(count)  # 0
print(data)   # {}: "count" 키는 추가되지 않음
```

`setdefault(키, 기본값)`는 키가 있으면 기존 값을 반환하고, 없으면 기본값을 실제 딕셔너리에 추가한 뒤 반환합니다.

```python
data = {}
quizzes = data.setdefault("quizzes", [])

print(quizzes)  # []
print(data)     # {"quizzes": []}: 키가 실제로 추가됨
```

이미 키가 있으면 값을 덮어쓰지 않습니다.

```python
data = {"best_score": 80}
score = data.setdefault("best_score", 0)

print(score)  # 80
print(data)   # {"best_score": 80}
```

따라서 단순 조회에는 `get()`을, 키가 없을 때 기본 구조까지 저장해야 한다면 `setdefault()`를 사용할 수 있습니다. 이번 프로젝트의 다음 코드는 저장 데이터에 `history`가 없을 때 빈 리스트를 만들어 넣습니다.

```python
self.history = self.data.setdefault("history", [])
```

딕셔너리의 자주 쓰는 기능:

| 기능 | 의미 |
| --- | --- |
| `key in data` | 키가 존재하는지 확인 |
| `data.keys()` | 모든 키 확인 |
| `data.values()` | 모든 값 확인 |
| `data.items()` | 키와 값을 쌍으로 확인 |
| `data.update(other)` | 다른 딕셔너리의 내용을 추가하거나 갱신 |
| `data.pop(key)` | 키에 해당하는 값을 꺼내며 삭제 |
| `del data[key]` | 키와 값을 삭제 |

```python
for key, value in quiz_data.items():
    print(key, value)

if "hint" in quiz_data:
    print(quiz_data["hint"])

deleted_hint = quiz_data.pop("hint", "힌트가 없습니다.")
```

`pop("hint", 기본값)`처럼 기본값을 함께 주면 키가 없어도 `KeyError`가 발생하지 않습니다.

#### tuple, set, None

`tuple`은 리스트처럼 순서가 있지만 만든 뒤 요소를 추가·수정·삭제할 수 없습니다.

```python
point = (10, 20)
print(point[0])  # 10
```

`set`은 순서를 기준으로 사용하지 않고 중복을 허용하지 않는 값의 모음입니다. 빈 세트는 `{}`가 아니라 `set()`으로 만듭니다. `{}`는 빈 딕셔너리입니다.

```python
answers = [1, 1, 2, 3, 3]
unique_answers = set(answers)

print(unique_answers)  # {1, 2, 3}, 출력 순서는 달라질 수 있음
unique_answers.add(4)
unique_answers.discard(1)  # 값이 없어도 오류가 나지 않음
```

`None`은 숫자 0이나 빈 문자열과 다른, **값이 없음**을 나타내는 특별한 값입니다.

```python
result = None

if result is None:
    print("아직 결과가 없습니다.")
```

`None`인지 확인할 때는 보통 `==`보다 `is None`, `is not None`을 사용합니다.

#### 변경 가능한 값과 변경 불가능한 값

- 변경 가능(mutable): `list`, `dict`, `set`
- 변경 불가능(immutable): `int`, `float`, `bool`, `str`, `tuple`

변경 가능한 값은 같은 객체의 내용을 바꿀 수 있습니다. 변수 두 개가 같은 리스트를 가리키면 한쪽에서 수정한 내용이 다른 쪽에서도 보입니다.

```python
original = [1, 2]
same_list = original
same_list.append(3)

print(original)  # [1, 2, 3]
```

독립된 리스트가 필요하면 `copy()`를 사용할 수 있습니다.

```python
original = [1, 2]
copied = original.copy()
copied.append(3)

print(original)  # [1, 2]
print(copied)    # [1, 2, 3]
```

요약:

> 자료형은 데이터의 종류이며 자료형마다 사용할 수 있는 기능이 다릅니다. 점수와 정답 번호는 int, 문제 문장은 str, 선택지와 퀴즈 목록은 list, 퀴즈 하나의 정보는 dict로 표현했습니다. 빈 문자열이나 빈 리스트, 숫자 0은 조건문에서 False처럼 판단되며, 데이터가 비었는지 확인할 때 이 성질을 활용할 수 있습니다.

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

요약:

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

요약:

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

#### 매개변수, 인자, 반환값

**매개변수(parameter)**와 **인자(argument)**는 비슷해 보이지만 사용하는 시점이 다릅니다.

- 매개변수: 함수를 정의할 때 값을 받을 자리에 붙인 이름
- 인자: 함수를 호출할 때 실제로 전달하는 값

```python
def greet(name):       # name은 매개변수
    print(f"{name}님 안녕하세요.")

greet("철수")          # "철수"는 인자
```

쉽게 말하면 매개변수는 빈칸의 이름이고, 인자는 그 빈칸에 실제로 넣는 값입니다.

##### 위치 인자와 키워드 인자

인자는 순서대로 전달하거나 매개변수 이름을 지정해서 전달할 수 있습니다.

```python
def introduce(name, age):
    print(f"{name}님은 {age}살입니다.")

introduce("철수", 20)              # 위치 인자: 순서가 중요함
introduce(age=20, name="철수")      # 키워드 인자: 이름으로 전달함
```

##### 기본값이 있는 매개변수

함수를 정의할 때 매개변수에 기본값을 지정하면, 호출할 때 해당 인자를 생략할 수 있습니다.

```python
def greet(name, message="안녕하세요"):
    print(f"{name}님, {message}.")

greet("철수")                 # 철수님, 안녕하세요.
greet("영희", "반갑습니다")   # 영희님, 반갑습니다.
```

기본값이 없는 매개변수를 먼저 쓰고, 기본값이 있는 매개변수를 뒤에 씁니다.

##### 반환값과 return

반환값은 함수가 작업을 끝낸 뒤 호출한 곳으로 돌려주는 결과입니다.

```python
def is_correct(user_answer, answer):
    return user_answer == answer

result = is_correct(2, 2)
print(result)  # True
```

`return`을 실행하면 함수는 즉시 끝납니다. `return`이 없거나 값 없이 `return`하면 함수의 반환값은 `None`입니다.

```python
def show_message():
    print("게임 시작")

result = show_message()
print(result)  # None
```

`print()`는 화면에 보여 주고, `return`은 값을 함수 밖에서 다시 사용할 수 있게 돌려준다는 차이가 있습니다.

##### 타입 힌트

타입 힌트는 매개변수와 반환값에 어떤 자료형을 기대하는지 적어 둔 안내입니다.

```python
def add_score(score: int, point: int) -> int:
    return score + point
```

- `score: int`: `score`에는 `int`를 기대함
- `point: int`: `point`에는 `int`를 기대함
- `-> int`: 함수가 `int`를 반환할 예정임

타입 힌트는 코드를 이해하고 실수를 찾는 데 도움을 주지만, Python이 실행 중에 타입을 자동으로 강제하거나 변환해 주는 것은 아닙니다.

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

여기서 `prompt`와 `msg`는 매개변수이고, `msg`에는 기본값이 있습니다. `-> str`은 문자열을 반환한다는 타입 힌트입니다.

```python
question = get_user_input(
    "문제: ",
    msg="문제를 비워둘 수 없습니다."
)
```

위 호출에서 `"문제: "`는 위치 인자이고 `msg="문제를 비워둘 수 없습니다."`는 키워드 인자입니다. 이 함수를 사용하면 문제 입력, 선택지 입력, 정답 입력에서 빈 문자열 검사를 반복해서 작성하지 않아도 됩니다.

요약:

> 함수는 특정 기능을 재사용할 수 있게 묶어 둔 코드입니다. 함수를 정의할 때 값을 받을 이름은 매개변수이고, 함수를 호출할 때 실제로 전달하는 값은 인자입니다. 이번 프로젝트에서는 입력 처리처럼 여러 곳에서 반복되는 로직을 함수로 분리해서 코드 중복을 줄였습니다.

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

요약:

> 클래스는 관련된 데이터와 기능을 묶는 설계도입니다. 퀴즈 게임에서는 문제, 선택지, 정답 같은 데이터를 Quiz 클래스로 묶고, 게임 진행과 저장은 QuizGame 클래스로 분리했습니다.

---

### 2. 객체와 인스턴스는 무엇인가

**객체(object)**는 Python 프로그램 안에서 다루는 값입니다. 숫자, 문자열, 리스트뿐 아니라 클래스로 직접 만든 값도 모두 객체입니다.

**인스턴스(instance)**는 "어떤 클래스로부터 만들어진 객체인가"를 강조하는 말입니다. 클래스가 설계도라면 인스턴스는 그 설계도로 만든 실제 제품입니다.

```python
quiz = Quiz(
    "Python의 창시자는?",
    ["Guido", "Linus", "Bjarne", "James"],
    1,
    "네덜란드 출신입니다."
)
```

위 코드의 관계를 정확히 말하면 다음과 같습니다.

- `Quiz`: 클래스
- `Quiz(...)`로 만들어진 값: 객체
- 그 객체는 `Quiz` 클래스의 인스턴스
- `quiz`: 그 객체를 가리키는 변수 이름

따라서 "`quiz`는 객체입니다"라고 말해도 일상적인 설명으로는 충분하고, "`quiz`가 가리키는 객체는 `Quiz` 클래스의 인스턴스입니다"라고 말하면 관계가 더 정확하게 드러납니다.

하나의 클래스에서 여러 인스턴스를 만들 수 있으며, 각 인스턴스는 서로 다른 속성값을 가질 수 있습니다.

```python
quiz1 = Quiz("1번 문제", ["A", "B", "C", "D"], 1, "힌트 1")
quiz2 = Quiz("2번 문제", ["A", "B", "C", "D"], 3, "힌트 2")

print(isinstance(quiz1, Quiz))  # True
print(isinstance(quiz2, Quiz))  # True
print(quiz1.answer)             # 1
print(quiz2.answer)             # 3
```

객체의 속성에 접근할 때는 점(`.`)을 사용합니다.

```python
print(quiz.question)
print(quiz.answer)
```

객체의 메서드도 점(`.`)으로 호출합니다.

```python
quiz.check_answer(1)
```

여기서 `quiz.question`은 속성 접근이고 `quiz.check_answer(1)`은 메서드 호출입니다.

요약:

> 객체는 Python에서 다루는 값이고, 인스턴스는 특정 클래스와 객체의 관계를 나타내는 말입니다. quiz가 가리키는 객체는 Quiz 클래스로 만든 객체이므로 Quiz의 인스턴스라고 할 수 있습니다.

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

요약:

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

## 8. 초보자를 위한 핵심 용어 사전

코드를 설명할 때 자주 사용하는 용어를 한곳에 정리했습니다.

### 값, 변수, 표현식, 문장

| 용어 | 쉬운 뜻 | 예시 |
| --- | --- | --- |
| 값(value) | 프로그램이 다루는 실제 데이터 | `10`, `"hello"`, `[1, 2]` |
| 변수(variable) | 값을 가리키기 위해 붙인 이름 | `score = 10`의 `score` |
| 할당(assignment) | 변수에 값을 연결하는 것 | `score = 10` |
| 표현식(expression) | 계산하면 하나의 값이 되는 코드 | `score + 10`, `answer == 1` |
| 문장(statement) | Python이 수행하는 하나의 명령 | `if`, `for`, `return`, 할당문 |

`score + 10`은 계산 결과가 나오는 표현식이고, `score = score + 10`은 그 결과를 다시 `score`에 할당하는 문장입니다.

### 여러 값을 다루는 용어

| 용어 | 쉬운 뜻 | 예시 |
| --- | --- | --- |
| 요소(element) | 리스트·튜플·세트 안의 값 하나 | `["A", "B"]`의 `"A"` |
| 인덱스(index) | 순서 있는 값의 위치 번호 | `choices[0]`의 `0` |
| 슬라이싱(slicing) | 연속된 일부 구간을 잘라 가져오기 | `choices[1:3]` |
| 키(key) | 딕셔너리에서 값을 찾는 이름표 | `quiz["answer"]`의 `"answer"` |
| 값(value) | 딕셔너리의 키와 짝을 이루는 데이터 | `{"answer": 1}`의 `1` |
| 길이(length) | 들어 있는 요소의 개수 | `len(choices)` |
| 순회(iteration) | 여러 값을 하나씩 꺼내며 반복하는 것 | `for choice in choices:` |
| 포함 여부(membership) | 어떤 값이 들어 있는지 확인하는 것 | `"A" in choices` |

### 함수와 관련된 용어

| 용어 | 쉬운 뜻 | 예시 |
| --- | --- | --- |
| 함수(function) | 특정 작업을 이름 붙여 묶은 코드 | `print()`, `len()`, `get_user_input()` |
| 호출(call) | 함수나 메서드를 실행하는 것 | `len(choices)` |
| 매개변수(parameter) | 함수 정의에서 값을 받을 이름 | `def greet(name)`의 `name` |
| 인자(argument) | 함수 호출 때 실제로 전달하는 값 | `greet("철수")`의 `"철수"` |
| 반환값(return value) | 함수가 호출한 곳으로 돌려주는 결과 | `len(choices)`의 결과 `4` |
| 내장 함수(built-in function) | Python이 기본으로 제공하는 함수 | `print()`, `input()`, `len()`, `type()` |
| 메서드(method) | 특정 객체에 속해 그 객체와 관련된 작업을 하는 함수 | `choices.append("A")` |

함수는 `len(choices)`처럼 이름으로 호출하고, 메서드는 `choices.append("A")`처럼 객체 뒤에 점을 붙여 호출하는 경우가 많습니다.

### 클래스와 관련된 용어

| 용어 | 쉬운 뜻 | 이번 프로젝트 예시 |
| --- | --- | --- |
| 클래스(class) | 데이터와 기능을 묶어 객체를 만드는 틀 | `Quiz`, `QuizGame` |
| 객체(object) | Python에서 다루는 하나의 값 | `Quiz(...)`로 만든 객체 |
| 인스턴스(instance) | 특정 클래스로 만들어졌음을 나타내는 객체 | `Quiz` 클래스의 인스턴스 `quiz` |
| 속성(attribute) | 객체가 가지고 있는 데이터 | `quiz.question`, `quiz.answer` |
| 메서드(method) | 객체가 수행할 수 있는 기능 | `quiz.display()`, `quiz.check_answer()` |
| 초기화(initialization) | 새 객체에 처음 필요한 상태를 넣는 과정 | `__init__`에서 문제와 정답 저장 |
| 참조(reference) | 변수가 객체를 가리키는 관계 | `quiz = Quiz(...)` |

### 프로그램 구조와 오류 관련 용어

| 용어 | 쉬운 뜻 | 예시 |
| --- | --- | --- |
| 모듈(module) | Python 코드를 담은 `.py` 파일 | `service/quiz.py` |
| 패키지(package) | 관련 모듈을 묶은 폴더 | `service` |
| import | 다른 모듈의 코드를 가져와 사용하는 문법 | `from service.quiz import Quiz` |
| 예외(exception) | 실행 중 발생한 문제를 나타내는 객체 | `ValueError`, `FileNotFoundError` |
| 예외 처리 | 예상 가능한 예외에 대응하는 것 | `try/except` |
| 버그(bug) | 프로그램이 의도와 다르게 동작하게 하는 코드 문제 | 점수가 잘못 계산되는 문제 |
| 디버깅(debugging) | 버그의 원인을 찾고 고치는 과정 | 값 출력, 오류 메시지 확인 |

---

## 9. 최종 점검 체크리스트

아래 질문에 답할 수 있으면 미션 목표를 잘 이해한 것입니다.

Python:

- 변수는 왜 필요한가?
- `int`, `str`, `bool`, `list`, `dict`는 각각 언제 사용하는가?
- 어떤 값들이 조건문에서 `False`처럼 판단되는가?
- `"0"`, `[0]`, `0`의 참/거짓 판단 결과는 각각 무엇인가?
- `append()`와 `extend()`의 차이는 무엇인가?
- 리스트를 수정하는 `sort()`의 반환값은 무엇인가?
- 딕셔너리에 키와 값을 추가하거나 수정하려면 어떻게 하는가?
- `data[key]`, `data.get(key, 기본값)`, `data.setdefault(key, 기본값)`은 어떻게 다른가?
- 변경 가능한 자료형과 변경 불가능한 자료형의 예를 들 수 있는가?
- `if / elif / else`는 어떤 상황에서 쓰는가?
- `for`와 `while`의 차이는 무엇인가?
- 함수의 매개변수와 인자는 어떻게 다른가?
- 위치 인자, 키워드 인자, 기본값이 있는 매개변수는 무엇인가?
- `print()`와 `return`은 어떻게 다른가?
- 타입 힌트는 무엇이며 실행 중 타입을 강제하는가?

클래스:

- 클래스, 객체, 인스턴스의 관계는 무엇인가?
- `quiz`는 객체인가, `Quiz`의 인스턴스인가?
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

## 10. 자주 헷갈리는 부분

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

### 비어 있는 값은 조건문에서 False처럼 판단된다

```python
print(bool(0))   # False
print(bool(""))  # False
print(bool([]))  # False
print(bool({}))  # False
```

하지만 안에 값이 하나라도 있으면 그 값 자체가 `0`이나 `False`여도 목록과 문자열은 비어 있지 않습니다.

```python
print(bool([0]))      # True
print(bool([False]))  # True
print(bool("0"))      # True
```

---

### append는 리스트를 바꾸지만 새 리스트를 반환하지 않는다

```python
choices = ["A", "B"]
result = choices.append("C")

print(choices)  # ["A", "B", "C"]
print(result)   # None
```

따라서 `choices = choices.append("C")`라고 작성하면 `choices`에 `None`이 저장되므로 주의합니다.

---

### get과 setdefault는 기본값을 다르게 다룬다

```python
data = {}

data.get("history", [])         # 빈 리스트를 반환만 함
print(data)                      # {}

data.setdefault("history", [])  # 빈 리스트를 반환하고 딕셔너리에도 추가함
print(data)                      # {"history": []}
```

조회만 필요하면 `get()`, 없는 키와 기본값을 딕셔너리에 저장해야 하면 `setdefault()`를 사용할 수 있습니다.

---

### 객체와 인스턴스는 서로 반대되는 말이 아니다

```python
quiz = Quiz("문제", ["A", "B", "C", "D"], 1, "힌트")
```

`quiz`가 가리키는 값은 객체이면서 동시에 `Quiz` 클래스의 인스턴스입니다. "객체"는 값 자체를 넓게 부르는 말이고, "인스턴스"는 어떤 클래스로 만들었는지를 강조하는 말입니다.

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
