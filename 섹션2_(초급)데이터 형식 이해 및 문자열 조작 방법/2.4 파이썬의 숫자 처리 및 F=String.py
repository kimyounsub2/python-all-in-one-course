# 반올림
print(round(8/3)) # 2.66666 에서 반올림하여 3

print(round(8/3, 3)) # 2.667 소숫점 3자리까지 나오고 4번재에서 반올림

print(round(2.66666, 2)) # 2.67

# 반버림
print(8//3) # 2.666666 에서 2

score = 0
## User scores a point

score += 1 # += : 1와 같이 -= : -1, *= : 0, /= : 0 이렇게도 할수 있다
print(score) # 1로 결과값이 나온다

#F-String 처리하기
score = 0 #정수
height = 1.8 #소수점
iswinning = True # 불리언

print("your score is " + str(score))
print(f"your score is {score}") # f를 입력해주면 모든 변수를 정수로 따로 변환안해줘도 된다

print(f"your score is {score}, your height is {height}, you are winning is {iswinning}")
#your score is 0, your height is 1.8, you are winning is True