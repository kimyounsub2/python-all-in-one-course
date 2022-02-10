
# Simple Function
def greet():
    print("Hello Youn")
    print("How do you do Kim Youn Sub?")
    print("Isn't the weather nice today?")
greet()

#Function that allows for input 입력값을(input) 받는 새로운 함수

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name} ?")
    
greet_with_name("김윤섭")
# 김윤섭이라는 데이터가 입력돼 name에 저장하고 두 출력물에 사용된것을 알수 있다.

# Functions with more than 1 input 위치 인자와 키워드 인자
# 여러 인자를 지정해서 순서와 상관없이 입력할수 있다.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
greet_with("김윤섭","서울")

# 여러 인자를 지정해서 순서와 상관없이 입력할수 있다.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
greet_with(location="김윤섭",name= "서울")