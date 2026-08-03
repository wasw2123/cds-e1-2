import json

DEFAULT_DATA = {                                                                                                                                                                                      
        "quizzes": [                                                                                                                                                                                      
            {                                                                                                                                                                                             
                "question": "파이썬(Python) 프로그래밍 언어를 만든 창시자는 누구일까요?",                                                                                                                 
                "choices": ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Bjarne Stroustrup"],                                                                                                  
                "answer": 1                                                                                                                                                                               
            },                                                                                                                                                                                            
            {                                                                                                                                                                                             
                "question": "파이썬에서 한 줄 주석을 작성할 때 사용하는 기호는 무엇일까요?",                                                                                                              
                "choices": ["//", "#", "/* */", "--"],                                                                                                                                                    
                "answer": 2                                                                                                                                                                               
            },                                                                                                                                                                                            
            {                                                                                                                                                                                             
                "question": "파이썬에서 변수의 데이터 타입을 확인할 때 사용하는 내장 함수는 무엇일까요?",                                                                                                 
                "choices": ["typeof()", "datatype()", "type()", "var_type()"],                                                                                                                            
                "answer": 3                                                                                                                                                                               
            },                                                                                                                                                                                            
            {                                                                                                                                                                                             
                "question": "다음 중 한 번 생성되면 요소를 변경할 수 없는(Immutable) 파이썬 자료형은 무엇일까요?",                                                                                        
                "choices": ["list", "dict", "set", "tuple"],                                                                                                                                              
                "answer": 4                                                                                                                                                                               
            },                                                                                                                                                                                            
            {                                                                                                                                                                                             
                "question": "파이썬 콘솔에 결과를 출력할 때 사용하는 함수는 무엇일까요?",                                                                                                                 
                "choices": ["console.log()", "print()", "System.out.println()", "echo()"],                                                                                                                
                "answer": 2                                                                                                                                                                               
            }                                                                                                                                                                                             
        ],                                                                                                                                                                                                
        "best_score": 0                                                                                                                                                                                   
    }                

class DataControl:

    def __init__(self):
        self.file_path = "state.json"
        self.encoding = "utf_8"
        self.ensure_ascii = False
        self.indent = 4

    def load_data(self):
        try:
            with open(self.file_path, "r", encoding=self.encoding) as f:
                return json.load(f)
                
        except (FileNotFoundError, json.JSONDecodeError):
            print("저장 파일이 손상되었습니다. 데이터를 초기화합니다.")
            return DEFAULT_DATA

    def save_data(self, data):                                                                                                                                                          
        with open(self.file_path, "w", encoding=self.encoding) as f:
            json.dump(data, f, ensure_ascii=self.ensure_ascii, indent=self.indent)

data_control = DataControl()