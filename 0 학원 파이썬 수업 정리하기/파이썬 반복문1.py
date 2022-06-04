# while 반복문
# 예제
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

i = 0
while i < 1000:
    print("%d : 안녕하세요? while 문을 공부 중입니다."%i)
    i = i + 1

# 1 ~ 10까지 합계 구하기
i, hap = 1,0
while i < 101:
    hap = hap + i
    i = i + 1
    # print("1에서 %d까지의 합계 : %d"%(i-1,hap))
    print(f"1에서 {i-1}까지의 합계 : {hap}")
print("1~10까지 총합은 %d" %hap)

# 무한 루프
while True:
    print("ㅋ ",end=" ")
# 무한루프를 사용하여 입력한 두 숫자의 합계를 반복해서 계산
hap = 0
a,b =0,0
while True:
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
    b = int(input("더할 두 번째 수를 입력하세요 : "))
    hap = a+ b
    print("%d + %d = %d" %(a, b, hap))
    

# 반복문을 탈출시키는 break 문
hap = 0
a,b =0,0
while True:
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
    if a ==0:
        break
    b = int(input("더할 두 번째 수를 입력하세요 : "))
    hap = a+ b
    print("%d + %d = %d" %(a, b, hap))
print("0을 입력해 반복문을 탈출했습니다.")

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# continue
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

a = 0
while a < 10:
    a = a + 1
    if a % 5 != 0: continue
    print(a)

# for문의 기본 구조
test_list = ['one','two', 'three']
for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다. " %number)

# for와 함께 자주 사용하는 range 함수
sum = 0
for i in range(1, 11):
    sum = sum +i
print(sum)

# for 문의 개념
# for 변수 in range(시작값, 끝값+1, 증가값):

for i in range(10,-1,-1):
    print("%d : 안녕하세요? for문을 공부 중입니다." %i)

for i in range(1, 6, 1):
    print("%d " %i, end ="")

i = 0
while i < 5:
    i += 1
    print("%d " %i, end ="")   

# 500과 1000 사이에 있는 홀수의 합계
i, hap = 0,0
for i in range(501, 1001, 2):
    hap = hap + i
print("500에서 1000 사이에 있는 홀수의 합계 : %d" %hap)

# 키보드로 입력한 수까지의 합계 구하기
i,hap = 0,0
num = 0

num = int(input("값을 입력하세요: "))
for i in range(1, num +1, 1):
    hap += i
print("1에서 %d까지의 합계 : %d" %(num,hap))

i,hap = 0,0
num1, num2, num3 = 0,0,0

num1 = int(input("시작값을 입력하세요: "))
num2 = int(input("끝값을 입력하세요: "))
num3 = int(input("증가값을 입력하세요: "))
for i in range(num1, num2 +1, num3):
    hap += i
print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" %(num1,num2,num3,hap))

# 구구단 만들기
i, dan = 0,0
dan = int(input("단을 입력하세요 : "))
for i in range(1, 10, 1):
    print("%d X %d = %d" % (dan,i,dan*i))
    
# 중첩 for문
for i in range(0,3,1):
    for k in range(0,2,1):
        print("파이썬은 꿀잼입니다.(i값 : %d, k값 : %d)" % (i,k))

# for문 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = ' ')
    print(' ')

# 리스트 내포(List comprehension)
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2, 10)
for y in range(1,10)]
print(result)

money = 0
a = int(input("구입 금액을 입력하시오: "))
if a > 100000:
    money = a * 0.05
    print("지불 금액은 %d" %money)
