
# def my_function(): 기본적으로 작성해야 하는 코드의 양을 줄이기 위함이고 반복적으로 실행하려는 명령어를 가지고 있을때
# dfr my_function(something): 입력을 감안하여 함수 내부의 코드를 수정하고 매번 다른 작업을 수행할수 있다.

#예제 1
def format_name(f_name, l_name): # 이 함수가 첫 번재 이름과 마지막 이름을 취하기 때문
    print(f_name.title()) # title 함수는 단어의 첫번째를 대문자로 변환시켜준다
    print(l_name.title())
    
format_name("kim youn sub", "KIM YOUN SUB") # 둘다 Kim Youn Sub 으로 단어의 첫글자만 대문자로 변환된다.

#예제 2
def format_name(f_name, l_name): 
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    
    print(f"{format_f_name}", f"{format_l_name}")
    
format_name("kim youn sub", "KIM YOUN SUB")

#예제 3
def format_name(f_name, l_name): 
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"{format_f_name} {format_l_name}"
    
formated_string = format_name("kim", "YOUN SUB")
print(formated_string)


