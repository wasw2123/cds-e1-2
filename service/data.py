import copy
import json

DEFAULT_DATA = {
    "quizzes": [
        {
            "question": "파이썬(Python) 프로그래밍 언어를 만든 창시자는 누구일까요?",
            "choices": ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Bjarne Stroustrup"],
            "answer": 1,
            "hint": "네덜란드 출신으로 파이썬의 창시자입니다."
        },
        {
            "question": "파이썬에서 한 줄 주석을 작성할 때 사용하는 기호는 무엇일까요?",
            "choices": ["//", "#", "/* */", "--"],
            "answer": 2,
            "hint": "영어로 '샤프' 또는 '파운드'라고 부르는 기호입니다."
        },
        {
            "question": "파이썬에서 변수의 데이터 타입을 확인할 때 사용하는 내장 함수는 무엇일까요?",
            "choices": ["typeof()", "datatype()", "type()", "var_type()"],
            "answer": 3,
            "hint": "타입을 반환하는 가장 간단한 내장 함수 이름입니다 (세 글자)."
        },
        {
            "question": "다음 중 한 번 생성되면 요소를 변경할 수 없는(Immutable) 파이썬 자료형은 무엇일까요?",
            "choices": ["list", "dict", "set", "tuple"],
            "answer": 4,
            "hint": "소괄호로 생성하며 수정이 불가능한 자료형입니다."
        },
        {
            "question": "파이썬 콘솔에 결과를 출력할 때 사용하는 함수는 무엇일까요?",
            "choices": ["console.log()", "print()", "System.out.println()", "echo()"],
            "answer": 2,
            "hint": "파이썬에서 표준 출력에 문자열을 보내는 내장 함수입니다."
        }
    ],
    "best_score": 0
}

class DataControl:

    def __init__(self):
        self.file_path = "state.json"
        self.encoding = "utf-8"
        self.ensure_ascii = False
        self.indent = 4

    def load_data(self):
        try:
            with open(self.file_path, "r", encoding=self.encoding) as f:
                return json.load(f)

        except FileNotFoundError:
            print("저장 파일이 없습니다. 기본 데이터로 초기화하고 파일을 생성합니다.")
            try:
                self.save_data(DEFAULT_DATA)
            except Exception as e:
                print(f"주의: 기본 데이터를 파일로 저장하지 못했습니다. 오류: {e}")
            return DEFAULT_DATA

        except json.JSONDecodeError:
            print("저장 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
            try:
                import os
                backup_path = self.file_path + ".bak"

                if os.path.exists(self.file_path):
                    os.replace(self.file_path, backup_path)
                    print(f"손상된 파일을 {backup_path}로 백업했습니다.")
                self.save_data(DEFAULT_DATA)

            except Exception as e:
                print(f"주의: 파일 백업 및 초기화 중 오류 발생. 오류: {e}")
                
            return DEFAULT_DATA

    def save_data(self, data):
        try:
            with open(self.file_path, "w", encoding=self.encoding) as f:
                json.dump(data, f, ensure_ascii=self.ensure_ascii, indent=self.indent)
        except Exception as e:
            print(f"데이터 저장 중 오류 발생: {e}")

    def quiz_data_reset(self, data):
        data["quizzes"] = copy.deepcopy(DEFAULT_DATA["quizzes"])
        print("퀴즈 데이터가 존재하지 않습니다.\n기본 퀴즈 데이터로 초기화합니다.")
        return data["quizzes"]


data_control = DataControl()