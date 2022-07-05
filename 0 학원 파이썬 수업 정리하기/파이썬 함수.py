# 함수
def add(a,b): # 매개변수
    return a + b
# 함수 활용 
a = 3
b = 4
c = add(a,b)
print(c)

# 함수 활용 
print(add(5,20)) # 인수
print(add(20,100))

def sub(a,b):
    return a - b
print(sub(88,10))

# 일반적인 함수
def sum(a,b):
    result = a + b
    return result
a = sum(3,4)
print(a)

# 입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)

# 결과값이 없는 함수
def sum(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
sum(3,4)

# 입력값도 결과값도 없는 함수
def say():
    print("Hi")
say()

# 기본 커피를 타는 과정의 코드
coffee = 0
coffee = int(input("어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))

print()
print("#1. 뜨거운 물을 준비한다.");
print("#2. 종이컵을 준비한다.");
      
if coffee == 1:
    print("#3. 보통커피를 탄다.")
elif coffee == 2:
    print("#3. 설탕커피를 탄다.")
elif coffee == 3:
    print("#3. 블랙커피를 탄다.")
else:
    print("#3. 아무거나 탄다.\n")

print("#4. 물을 붓는다.");
print("#5. 스푼을 젓는다.");
print();
print("손님 ~ 커피 여기 있습니다.");

# 함수 이용 자판기 만들기
# 전역 변수 선언
coffee = 0
# 함수 선언 부분
def coffee_machine(button):
    print()
    print("#1. 뜨거운 물을 준비한다.");
    print("#2. 종이컵을 준비한다.");
          
    if coffee == 1:
        print("#3. 보통커피를 탄다.")
    elif coffee == 2:
        print("#3. 설탕커피를 탄다.")
    elif coffee == 3:
        print("#3. 블랙커피를 탄다.")
    else:
        print("#3. 아무거나 탄다.\n")
    
    print("#4. 물을 붓는다.");
    print("#5. 스푼을 젓는다.");
    print();
# 메인 코드
coffee = int(input("어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("손님 ~ 커피 여기 있습니다.");

# 함수 활용하여 연속해서 방문한 손님(A,B,C) 3명에게 커피 대접
coffee = int(input("A손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("A손님 ~ 커피 여기 있습니다.");

coffee = int(input("B손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("B손님 ~ 커피 여기 있습니다.");

coffee = int(input("C손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("C손님 ~ 커피 여기 있습니다.");

# 예제
coffee = 0
def coffee_sub(p):
    print()
    print("#1. 뜨거운 물을 준비한다.");
    print("#2. 종이컵을 준비한다.");
          
    if coffee == 1:
        print("#3. 아메리카노를 탄다.")
    elif coffee == 2:
        print("#3. 까페라떼를 탄다.")
    elif coffee == 3:
        print("#3. 카푸치노를 탄다.")
    elif coffee == 4:
        print("#3. 에스프레소를 탄다.")
    else:
        print("#3. 아무거나 탄다.\n")
    
    print("#4. 물을 붓는다.");
    print("#5. 스푼을 젓는다.");
    print();
    
name = ["로제","리사","지수","제니"]
for i in name:
    coffee = int(input("%s씨, 어떤 커피 드릴까요?(1:아메리카노, 2:까페라떼, 3:카푸치노, 4:에스프레소)"%i))
    coffee_sub(coffee)
    print("%s씨 ~ 커피 여기 있습니다."%i);

# plus() 함수
def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = 0

hap = plus(100,200)
print("100과 200의 plus() 함수 결과는 %d"%hap)

def calc(v1,v2,op):
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/' :
        result = v1/v2
    return result
    
res, var1, var2, oper = 0,0,0,""

oper = input("계산을 입력하세요(+,-,*,/) : ")
var1 = int(input("첫 번째 수를 입력하세요 : "))
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1, var2, oper)
print("## 계산기 : %d %s %d = %d" %(var1, oper, var2, res))

# 반환값이 없는 함수
def func1():
    result = 100
    return result

def func2():
    print("반환값이 없는 함수 실행")
hap = 0
hap = func1()
print("func1()에서 돌려준 값 ==>%d" % hap)
func2()
    
# 프로그램 완성
import random
def getNumber():
    return random.randrange(1,46)

lotto = []
num = 0
print("** 로또 추첨을 시작합니다. **\n");

while True:
    num = getNumber()
    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto) >=6:
        break
print("추첨된 로또 번호 ==> ", end = '')
lotto.sort()
for i in range(0, 6):
    print("%d " %lotto[i], end = '')

# 함수 여러 개의 입력값 : 입력값이 몇 개든 상관없이 처리한다.
def sum_many(*args): # *args 입력변수 앞에 *을 붙이면 입력 값들을 전부 모아 튜플로 만들어 줌
    sum = 0
    for i in args:
        sum = sum +i
    return sum
result = sum_many(1,2,3)
print(result)
result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def add_nul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = add_nul('add',1,2,3,4,5)
print(result)

result = add_nul('mul',1,2,3,4,5)
print(result)

# 함수의 결과값은 언제나 하나이다.
### 1.
def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
print(result)
### 2.
def add_and_mul(a,b):
    return a+b
    return a*b

result = add_and_mul(3,4)
print(result)

# 입력 인수에 초깃값 미리 설정하기
# 기본 값을 지정한 입력 인수는 모든 입력 인수 중 마지막에만 사용할 수 있음
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박응용", 27)
say_myself("박응용", 27, True)

# 함수 안에서 선언된 변수의 효력 범위
# 함수 내부에서 선언된 변수는 함수 안에서만 사용할수 있음 -> 지역변수
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a) # 함수 안의 a와 함수 밖의 a는 별개의 변수
# 함수 안에서 함수 밖의 변수를 변경하는 방법 1
a = 1
def vartest(a):
    a = a + 1
    return a
vartest(a)
print(a)
# 함수 안에서 함수 밖의 변수를 변경하는 방법 1
a = 1
def vartest(a):
    # global a
    a = a + 1
vartest(a)
print(a)

def func1():
    # global a # 이 함수 안에서 a는 전역 변수
    a = 10
    print("func1()에서 a값 %d" %a)
    
def func2():
    print("func2()에서 a값 %d"%a)

a = 20 # 전역 변수
func1()
func2()
