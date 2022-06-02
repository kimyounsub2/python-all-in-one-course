# 제어문 if
money = 0
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

a = 99
if a < 100:
    print("100보다 작군요.")
    
x = 3
y = 2
x > y
x < y
x == y
x != y

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
    
test = int(input("정수를 입력하세요: "))
if test % 2 == 0:
    print("짝수를 입력했군요")
else:
    print("홀수를 입력했군요")


money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


d = float(input("연재 기온을 입력하시오: "))
if d >= 30:
    print("반바지를 입으세요")
else:
    print("긴바지를 입으세요")
print("이제 나가서 운동하세요!")

# x in s, x not in s -> 리스트
1 in [1, 2, 3] # 1이 안에 있는가?
1 not in [1, 2, 3] # 1이 안에 없는가?
'a' in ('a', 'b', 'c')
'j' not in 'python'

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone', 'money']
if 'card' not in pocket:
    print("걸어가라")
else:
    print("버스를 타고 가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# 중첩 if문
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:    
        print("걸어가라")


# 다중 조건 판단 elif
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("돈을 내고 택시를 타고가라")
elif card:
    print("카드를 내고 택시를 타고가라")
else:
    print("걸어가라")

score = int(input("점수를 입력하세요 : "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("D")
elif score >= 60:
    print("D")
else:
    print("F")
print("학점입니다. ^^")

year = int(input("당신이 태어난 연도를 입력하세요. "))
age = 2022 - int(year) +1

if 20 <= age < 27:
    print("나이는 %d세 대학생입니다." %age)
elif 17 <= age < 20:
    print("나이는 %d세 고등학생입니다." %age)
elif 14 <= age < 17:
    print("중학생")
elif 8 <= age < 14:
    print("초등학생")
else:
    print("나이는 %d세 학생이 아닙니다." %age)

# 조건식 표현식
scoer = 50
if scoer >=60:
    message = "success"
else:
    message = "failuer"
print(message)
# 파이썬의 조건부 표현식(conditional expression)을 사용
scoer = 50
message = "success" if score >= 60 else "failure"
print(message)
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# 삼항 연산자를 사용한 if문
# 예제 1
jumsu = 55
res = ''
if jumsu >= 60:
    res = '합격'
else:
    res = '불합격'
print(res)
# 예제 2 단 한줄로 if문을 사용할 수 있다.
jumsu = 55
res = ''
res = '합격' if jumsu >= 60 else '불합격'
print(res)  
