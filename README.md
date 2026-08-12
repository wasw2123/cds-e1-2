# 🎯 나만의 퀴즈 게임 (Python 콘솔)

요약  
터미널에서 실행되는 Python 퀴즈 게임입니다. 문제 풀기, 문제 추가, 문제 목록, 최고 점수 조회, 문제 삭제, 게임 기록을 제공합니다. 데이터는 프로젝트 루트의 `state.json`에 JSON(UTF-8)으로 저장되어 프로그램 종료 후에도 유지됩니다.

주제 및 선정 이유  
- 주제: Python 기초 (변수, 자료형, 함수, 클래스, 파일 입출력 등)  
- 이유: 수업 목표가 Python 기초 실습이므로 직접 퀴즈를 만들어 풀며 문법과 흐름을 반복 학습하기에 적합합니다.

요구사항(환경)
- Python 3.13
- 외부 라이브러리 없음 (표준 라이브러리만 사용)
- 실행: 터미널에서 `python main.py` (또는 `python3 main.py`)

주요 기능
- 메뉴(숫자 입력)로 조작
- 퀴즈 풀기(랜덤 출제, 문제 수 선택, 힌트 사용: 점수 차감)
- 퀴즈 추가(문제 + 선택지 4개 + 정답 입력/검증)
- 퀴즈 목록 보기(저장된 모든 문제 표시)
- 문제 삭제
- 최고 점수 확인 및 기록 갱신 (state.json에 저장)
- 게임 기록 저장(날짜/문제수/점수)
- 입력 오류/예외 처리 (빈 입력, 숫자 변환 오류, 범위 벗어남, Ctrl+C / EOF 처리)
- 데이터 손상 시 기본 퀴즈로 복구

파일 구조 (주요)
- main.py — 진입점(프로그램 실행)
- service/
  - core.py - 공통으로 사용할 수 있는 함수
  - quiz.py — Quiz 클래스 (question, choices, answer, hint + 출력/체크 메서드)
  - game.py — QuizGame 클래스 (메뉴/플레이/추가/목록/점수/삭제/저장/불러오기)
  - data.py — state.json 입출력과 초기화 로직
- state.json — 저장된 퀴즈와 최고점/기록 (프로젝트 루트)
- docs/ — 스크린샷 및 문서

## 클래스 사용 이유

퀴즈의 데이터와 동작을 역할별로 묶고 책임을 분리하기 위해 클래스를 사용했습니다. `Quiz`는 문제, 선택지, 정답, 힌트와 같은 한 문제의 상태 및 출력·정답 확인을 담당하고, `QuizGame`은 메뉴, 게임 진행, 점수와 퀴즈 목록 관리를 담당합니다. `DataControl`은 `state.json` 저장과 불러오기를 담당합니다.

함수만 사용하면 퀴즈 데이터와 여러 함수에 전달할 인자가 흩어질 수 있지만, 클래스는 관련된 속성과 메서드를 한 객체에 묶을 수 있습니다. 따라서 역할과 책임이 명확해지고, 여러 퀴즈 객체를 같은 방식으로 다루기 쉬우며, 힌트나 기록 같은 기능을 확장하기도 편리합니다. 반면 상태를 가지지 않는 단순 입력 처리처럼 독립적인 작업은 `get_user_input()`과 같은 함수로 분리했습니다.

## JSON 저장 선택 이유와 장단점

JSON은 퀴즈 목록과 최고 점수처럼 구조화된 데이터를 `dict`와 `list`에 가까운 형태로 저장할 수 있고, `json.load()`로 불러온 뒤 `quizzes`, `best_score` 같은 키를 통해 원하는 값에 쉽게 접근할 수 있어 선택했습니다. 텍스트 형식이라 사람이 읽고 확인하기 쉬운 가독성이 있으며, 별도의 서버나 외부 라이브러리 없이 파일 하나로 관리할 수 있어 소규모 프로젝트에서 경량성도 좋습니다.

다만 JSON은 데이터를 읽거나 저장할 때 현재 구조상 파일 전체를 처리해야 하고, 데이터 검색·부분 수정·동시 접근에는 적합하지 않습니다. 데이터가 많아지거나 검색과 수정이 빈번해지면 데이터베이스가 더 적합합니다.

## state.json 스키마와 설계 이유

`state.json`은 퀴즈, 최고 점수, 플레이 기록을 하나의 최상위 객체에 저장합니다.

```json
{
    "quizzes": [
        {
            "question": "Python의 창시자는?",
            "choices": ["Guido", "Linus", "Bjarne", "James"],
            "answer": 1,
            "hint": "선택적 힌트 문자열"
        }
    ],
    "best_score": 0,
    "history": [
      {
            "timestamp": "2026-08-05 17:38:49",
            "questions": 1,
            "score": 9
        }
    ]
}
```

- `quizzes`: 여러 문제를 순서대로 관리해야 하므로 배열로 저장합니다.
- `question`: 문제 문장을 저장하는 문자열입니다.
- `choices`: 한 문제에 속한 선택지 4개를 순서대로 유지하기 위해 배열로 저장합니다.
- `answer`: `choices`의 정답 번호를 1~4의 정수로 저장합니다.
- `hint`: 문제별 힌트를 저장하는 문자열입니다.
- `best_score`: 지금까지의 최고 점수를 빠르게 확인할 수 있도록 최상위 정수 필드로 저장합니다.
- `history`: 게임을 여러 번 실행한 기록을 보존하기 위한 배열입니다.
- `timestamp`, `questions`, `score`: 한 번의 플레이 시각, 출제 문제 수, 획득 점수를 하나의 기록 객체로 묶습니다.

퀴즈마다 선택지·정답·힌트가 함께 움직여야 하므로 하나의 퀴즈 객체 안에 중첩했습니다. 플레이 기록도 한 게임에서 발생한 값들을 하나의 객체로 묶어 `history` 배열에 추가합니다. 이 구조는 서로 관련된 데이터가 흩어지지 않고, 퀴즈 추가·삭제와 기록 조회 시 한 단위로 처리되도록 합니다.

## 데이터 증가 시 한계와 개선 방향

현재 프로그램은 시작할 때 `state.json` 전체를 메모리에 불러오고, 내용이 변경되면 파일 전체를 다시 저장합니다. 문제 수가 적을 때는 구현이 간단하고 속도도 충분하지만, 문제가 1,000개 이상으로 증가하면 파일 크기와 메모리 사용량이 함께 늘고 시작 및 저장 시간이 길어질 수 있습니다. 문제 하나를 추가하거나 수정할 때도 전체 JSON을 다시 써야 하며, 특정 조건의 문제를 찾으려면 목록을 순차 검색해야 합니다.

문제가 수천~수만 개로 커지거나 검색·수정이 자주 필요하다면 SQLite 같은 데이터베이스로 전환할 수 있습니다. 데이터베이스를 사용하면 필요한 문제만 조회하거나 한 행만 수정할 수 있고, 인덱스를 통해 검색 성능을 개선할 수 있습니다. 따라서 현재 JSON 방식은 소규모 학습 프로젝트에 적합하고, 대규모 데이터에서는 DB 전환이 개선 방안입니다.

실행 방법 예시
1. 터미널 열기
2. 프로젝트 루트로 이동
3. Python 3.13+가 설치되어 있으면:
   python main.py
(Windows: python, macOS/Linux: python3 필요한 경우 사용)

## Git 커밋 규칙

커밋은 나중에 변경 이유를 쉽게 찾고 문제가 생겼을 때 기능 단위로 되돌릴 수 있도록, 하나의 기능 또는 하나의 목적을 기준으로 나눕니다. 예를 들어 메뉴 구현, 퀴즈 추가, 점수 처리, 예외 처리, 문서 작성은 각각 별도 커밋으로 관리합니다. 서로 관련 없는 코드와 문서 변경을 한 커밋에 섞지 않습니다.

커밋 메시지는 `<종류>: <변경 내용>` 형식을 사용하며, 변경한 내용을 구체적으로 작성합니다.

- `Feat: 퀴즈 출제 기능 구현`
- `Fix: 메뉴 범위 밖 입력 처리`
- `Docs: README 실행 방법 추가`
- `Refactor: QuizGame 책임 분리`

## 브랜치와 병합

브랜치는 안정적인 `main` 코드와 새 기능 작업을 분리하기 위한 독립적인 작업 공간입니다. 기능별 브랜치를 사용하면 개발 중인 코드가 `main`에 바로 영향을 주지 않고, 기능별 변경 이력을 구분할 수 있습니다. 병합(merge)은 브랜치에서 완성한 변경사항을 `main`과 같은 대상 브랜치에 합치는 작업입니다.

이 프로젝트에서는 `feat/random`, `feat/select_q_count`, `refactor/game` 등의 브랜치에서 기능을 작업하고 검증한 뒤 `main`으로 병합했습니다. 기본 사용 흐름은 다음과 같습니다.

```bash
git checkout -b feat/play-quiz
# 기능 작성 및 확인
git add service/game.py
git commit -m "Feat: 퀴즈 출제 기능 구현"
git checkout main
git merge feat/play-quiz
```

제출 및 증빙 항목
- GitHub 저장소 URL
  https://github.com/wasw2123/cds-e1-2
- 개발환경 스크린샷 (VSCode, Python 버전, git config)
![개발환경](./docs/screenshots/CleanShot%202026-08-05%20at%2022.13.59.png)
- 프로그램 실행 스크린샷: 메뉴, 플레이, 추가, 점수 등 (docs/screenshots 폴더 권장)
![실행 및 메뉴 진입](./docs/screenshots/CleanShot%202026-08-05%20at%2022.45.20.png)
![게임 시작, 문제 수 선택](./docs/screenshots/CleanShot%202026-08-05%20at%2022.46.58.png)
![힌트](./docs/screenshots/CleanShot%202026-08-05%20at%2022.48.03.png)
![정답 및 복귀](./docs/screenshots/CleanShot%202026-08-05%20at%2022.48.32.png)
![문제 추가](./docs/screenshots/CleanShot%202026-08-05%20at%2022.52.42.png)
![문제 추가 확인](./docs/screenshots/CleanShot%202026-08-05%20at%2022.53.23.png)
![문제 목록 조회](./docs/screenshots/CleanShot%202026-08-05%20at%2022.54.23.png)
![최고 점수 조회](./docs/screenshots/CleanShot%202026-08-05%20at%2022.54.55.png)
![문제 삭제 진입](./docs/screenshots/CleanShot%202026-08-05%20at%2022.55.51.png)
![문제 삭제 완료](./docs/screenshots/CleanShot%202026-08-05%20at%2022.56.33.png)
![기록 조회](./docs/screenshots/CleanShot%202026-08-05%20at%2022.57.44.png)
![종료](./docs/screenshots/CleanShot%202026-08-05%20at%2022.58.15.png)
- git log --oneline --graph 스크린샷
![git log](./docs/screenshots/CleanShot%202026-08-05%20at%2022.59.02.png)

- git clone
![git clone](./docs/screenshots/CleanShot%202026-08-10%20at%2011.48.31.png)
![git pull origin main - 상태 최신화](./docs/screenshots/CleanShot%202026-08-10%20at%2011.51.39.png)
![README 수정 on stage](./docs/screenshots/CleanShot%202026-08-10%20at%2011.54.33.png)
![커밋, 깃허브에 반영(push)](./docs/screenshots/CleanShot%202026-08-10%20at%2011.55.06.png)
![업데이트된 내용 반영](./docs/screenshots/CleanShot%202026-08-10%20at%2011.55.35.png)

Repository 상태(빠른 검사 결과)
- state.json: 존재 — quizzes 5개 포함 (요구: 5개 이상) ✅
- Quiz 클래스: service/quiz.py에 존재 ✅
- QuizGame 클래스: service/game.py에 존재, 메뉴/메서드 분리 확인 ✅
- 데이터 저장 위치: 프로젝트 루트의 state.json ✅
- 커밋 수: 20개 (요구 ≥10) ✅
- 브랜치: 여러 feature 브랜치 존재 (feat/q_list, feat/random 등) — 브랜치 생성 기록 있음 ✅
- 병합: main에 여러 브랜치가 merged 목록에 포함(merged branches 확인) ✅
- remote origin: git@github.com:wasw2123/cds-e1-2.git (remote 존재) ✅
- clone / pull 사용 여부: git_clone dir에 수행 ✅
