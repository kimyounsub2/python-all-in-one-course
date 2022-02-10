#num_char = len(input("What is your name?"))
# print("Your name has " + num_char + "characters.") # ""문자열 안에 len 함수 숫자가 들어갈수 없다

#print(type(num_char)) # num_char라는 변수가 정수인지 실수인지 출력해준다 답 int 정수


num_char = len(input("What is your name?"))

new_num_char = str(num_char) # 정수 데이터인 num_char를 받아서 str함수의 괄호 안에 넣었고 문자열로 변환했고 새로운 변수 이름으로 저장

print("Your name has " + new_num_char + " characters.")

#정수타입인 int
a = 123
print(type(a))

# str함수를 통해 정수(int)를 문자열(string)로 변환
a = str(123)
print(type(a))

# float함수는 소수형태로 변환
a = float(123)
print(type(a))

print(70 + float("100.5")) # 170.5 

print(str(70) + str(100)) # 둘다 문자열로 변환하여 70100