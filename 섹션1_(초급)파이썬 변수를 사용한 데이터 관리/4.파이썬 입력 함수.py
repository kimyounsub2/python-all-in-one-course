print("What is your name?")
#print는 what is your name이라는 출력물을 완전히 끄내지만

input("What is your name?") 
#input은 what is your name 이 입력 코드가 실행되면, 사용자가 youn이라는 입력한 데이터가 입력 코드의 youn으로 대체한다

print("Hello " + input("What is your name?"))
# 먼저 What is your name?을 물어보고 youn을 입력하면 Hello youn이라고 입력된다
#input은 ()안의 사용자 자 입력값을=youn을 가져오고 Print()가 Hello라는 단어와 사용자 입력을 출력한다.

print(len("kimyounsub")) #len은 문자의 숫자를 알려준다

print(len(input("What is your name")))