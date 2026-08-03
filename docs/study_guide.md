# 📚 파이썬 & Git 핵심 개념 및 코드 예시 가이드

이 문서는 프로그래밍을 처음 접하는 사람에게 개념을 쉽게 설명할 수 있도록 **쉬운 비유**, **핵심 설명**, **실제 파이썬/Git 코드 예시**를 정리한 가이드입니다.

---

## 1. Python 기초 개념

### 1) 변수 (Variable)
* **🎨 쉬운 비유**: **[라벨(이름표)이 붙은 수납 상자]**
* **💡 설명 멘트**:  
  "컴퓨터 메모리에 데이터를 저장하고, 필요할 때마다 꺼내 쓸 수 있도록 이름표를 붙여두는 것입니다."
* **💻 코드 예시**:
```python
score = 80          # score라는 이름표를 붙인 상자에 숫자 80 저장
user_name = "철수"  # user_name이라는 이름표를 붙인 상자에 문자열 "철수" 저장

print(score)        # 80 출력
```

---

### 2) 기본 자료형 (`int`, `str`, `bool`, `list`, `dict`)
* **🎨 쉬운 비유**: **[상자 속에 담긴 내용물의 종류]**
* **💻 코드 예시**:
```python
# 1. int (정수) - 계산 가능한 숫자
age = 25

# 2. str (문자열) - 따옴표로 감싸진 글자
quiz_title = "영화 '기생충'의 감독은?"

# 3. bool (참/거짓) - True / False 스위치
is_correct = True

# 4. list (리스트) - 순서(index)가 있는 서랍장
choices = ["1. 박찬욱", "2. 봉준호", "3. 김기덕", "4. 이창동"]
print(choices[1])  # "2. 봉준호" 출력 (0부터 시작)

# 5. dict (딕셔너리) - [키(Key) : 값(Value)] 짝을 이루는 보관함
quiz_data = {
    "question": "파이썬의 창시자는?",
    "answer": 1
}
print(quiz_data["question"])  # "파이썬의 창시자는?" 출력
```

---

### 3) 조건문 (`if / elif / else`)
* **🎨 쉬운 비유**: **[인생의 갈림길 / 신분증 검사]**
* **💡 설명 멘트**:  
  "상황(조건)에 따라 컴퓨터가 수행할 코드의 방향을 결정하는 갈림길입니다."
* **💻 코드 예시**:
```python
answer = 2
user_input = int(input("정답 번호를 입력하세요 (1-4): "))

if user_input == answer:
    print("✅ 정답입니다!")
elif user_input < 1 or user_input > 4:
    print("⚠️ 1번부터 4번 사이의 숫자를 입력해주세요.")
else:
    print("❌ 틀렸습니다.")
```

---

### 4) 반복문 (`for` vs `while`)
* **🎨 쉬운 비유**: **[시험지 5장 다 검사하기(`for`)] vs [퇴근 시간 될 때까지 무한 일하기(`while`)]**
* **💻 코드 예시**:
```python
# for: 퀴즈 3문제가 담긴 리스트의 요소를 순서대로 1개씩 꺼내며 3번 반복
quizzes = ["문제1: ...", "문제2: ...", "문제3: ..."]
for q in quizzes:
    print(q)

# while: 사용자가 "5"를 입력해서 종료할 때까지 메뉴판을 무한히 반복 출력
while True:
    print("1. 퀴즈 풀기  5. 종료")
    menu = input("선택: ").strip()
    if menu == "5":
        print("프로그램을 종료합니다.")
        break  # while 반복문을 탈출(종료)
```

---

### 5) 함수 (Function)
* **🎨 쉬운 비유**: **[자판기 / 전자레인지]**
* **💡 설명 멘트**:  
  "재료(매개변수)를 넣으면 정해진 조리를 거쳐 결과(반환값)를 내놓는 독립된 도구입니다."
* **💻 코드 예시**:
```python
# 함수 정의: def 함수이름(매개변수):
def calculate_score(correct_count, total_count):
    score = (correct_count / total_count) * 100
    return score  # 계산된 점수를 반환

# 함수 호출
final_score = calculate_score(4, 5)  # 4개 정답 / 5문제 총합
print(f"최종 점수: {final_score}점")   # "최종 점수: 80.0점"
```

---

## 2. 클래스와 객체 (객체지향 OOP)

### 1) 클래스(Class), 객체(Object), `__init__`, `self`
* **🎨 쉬운 비유**: **[붕어빵 틀(설계도)] vs [구워낸 붕어빵(실체)]**
* **💻 코드 예시**:
```python
class Quiz:
    # __init__: 객체가 생성될 때 자동으로 실행되어 속성을 초기화하는 메서드(생성자)
    # self: 생성된 "객체 자신"을 가리키는 손가락
    def __init__(self, question, choices, answer):
        self.question = question   # 속성(Attribute): 질문 데이터
        self.choices = choices     # 속성(Attribute): 선택지 리스트
        self.answer = answer       # 속성(Attribute): 정답 번호

    # 메서드(Method): 객체가 실행할 수 있는 기능/동작
    def check_answer(self, user_choice):
        return user_choice == self.answer

    def display(self):
        print(f"[문제] {self.question}")
        for choice in self.choices:
            print(choice)

# --- 객체(Object / Instance) 생성 ---
q1 = Quiz(
    question="파이썬의 창시자는?",
    choices=["1. Guido", "2. Linus", "3. Bjarne", "4. James"],
    answer=1
)

# 객체의 속성에 접근 및 메서드 호출
q1.display()                     # 문제 및 선택지 출력
is_right = q1.check_answer(1)    # True 반환
```

---

## 3. 파일 입출력 & 예외 처리

### 1) 파일 입출력 & JSON (`json.dump`, `json.load`)
* **🎨 쉬운 비유**: **[표준 공용 데이터 서류첩을 열고 읽고 쓰기]**
* **💻 코드 예시**:
```python
import json

# 1. 파일에 데이터 저장하기 (Write)
game_state = {
    "best_score": 80,
    "quizzes": [
        {"question": "파이썬 창시자는?", "choices": ["Guido", "Linus", "Bjarne", "James"], "answer": 1}
    ]
}

with open("state.json", "w", encoding="utf-8") as f:
    json.dump(game_state, f, ensure_ascii=False, indent=4)

# 2. 파일에서 데이터 불러오기 (Read)
with open("state.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(loaded_data["best_score"])  # 80 출력
```

---

### 2) 예외 처리 (`try - except`)
* **🎨 쉬운 비유**: **[자동차 에어백 / 비상 안전장치]**
* **💡 설명 멘트**:  
  "에러가 생겨도 프로그램이 튕기지 않도록 예외 상황을 포착해 처리하는 안전장치입니다."
* **💻 코드 예시**:
```python
# 1. 숫자가 아닌 입력 예외 방어
try:
    user_num = int(input("숫자를 입력하세요: ").strip())
except ValueError:
    print("⚠️ 숫자가 아닙니다! 1~5 사이의 숫자를 입력해주세요.")

# 2. 파일 부재 또는 Ctrl+C 예외 방어
try:
    with open("state.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("📂 저장된 파일이 없어 기본 데이터로 시작합니다.")
except KeyboardInterrupt:
    print("\n⚠️ 사용자에 의해 프로그램이 중단되었습니다. 데이터를 저장하고 종료합니다.")
```

---

## 4. Git & GitHub 필수 명령어 예시

```bash
# 1. Git 저장소 초기화
git init

# 2. 기능 작성을 위한 새 브랜치 생성 및 이동
git checkout -b feature/quiz-play

# 3. 변경사항을 커밋 대기 상태(Staging Area)로 올리기
git add main.py README.md

# 4. 의미 있는 단위로 커밋(스냅샷) 생성
git commit -m "Feat: 퀴즈 풀기 기능 구현"

# 5. 메인 브랜치로 돌아와서 작업한 브랜치 병합
git checkout main
git merge feature/quiz-play

# 6. GitHub 원격 저장소로 푸시
git push origin main

# 7. 원격 저장소 복제 및 최신 변경사항 가져오기
git clone https://github.com/your-id/repository-name.git
git pull origin main
```
