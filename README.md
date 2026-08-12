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

state.json 스키마 예시
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

실행 방법 예시
1. 터미널 열기
2. 프로젝트 루트로 이동
3. Python 3.13+가 설치되어 있으면:
   python main.py
(Windows: python, macOS/Linux: python3 필요한 경우 사용)

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
- 커밋 수: 13개 (요구 ≥10) ✅
- 브랜치: 여러 feature 브랜치 존재 (feat/q_list, feat/random 등) — 브랜치 생성 기록 있음 ✅
- 병합: main에 여러 브랜치가 merged 목록에 포함(merged branches 확인) ✅
- remote origin: git@github.com:wasw2123/cds-e1-2.git (remote 존재) ✅
- clone / pull 사용 여부: git_clone dir에 수행 ✅