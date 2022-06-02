
# 숫자 바로 대입
"I eat %d apples." % 3
# 문자열 바로 대입
"I eat %s applse." %"Five"
# 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." %number

# 문자열 포매팅
number = 10 
day = "three"
"I ate %d apples. so I was sick for %s datys." % (number,day)

# s가 문자열이지만 정수와 소수값 상관없이 찍힌다.
"I have %s apples" %3
"rate is %s" %3.234

# 소수점 표현
"%0.4f" %3.42134234 # 소수점 4자리까지 표현
"%5.4f" % 3.42134234 # 전체 5자리중에 소수점 4자리 표현
"%10.4f" % 3.42134234 # 전체 10자리중에 소수점 4자리 표현

# 정렬과 공백
"%10s" %"hi" # 전체 길이가 10개인 문자열 공간에서 hi를 오른쪽으로 정렬
"%-10sjane." % 'hi' # 왼쪽 정렬

name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다'

age = 30
f'나는 내년이면 {age+1}살이 된다.'

# 숫자로 바로 대입하기
"I eat {0} apples".format(3)
"I eat {0} apples".format("five")

number = 3
"I eat {0} apples". format(number)

# 2개 이상의 값을 넣을때
number = 10
day ="three"
"I ate {0} apples. so I was sick for {1} day".format(number,day)

print("100") # 문자 100
print("%d" % 100) # 숫자 100

print("100 + 100")
print("%d" %(100+100))

print("%d" % (100,200))
print("%d %d" % (100))

print("%d / %d = %0.1f" %(100,200,0.5))

# print 함수를 사용한 깔끔한 출력
print("%d" % 123) # 숫자의 자리만큼 정렬
print("%5d" % 123) # 오른쪽에 붙여서 정렬
print("%05d" % 123) # 오른쪽에 붙여서 정렬 빈칸을 0으로 채움
print("%f" % 123.45) # 소수점 아래 여섯자리까지 무조건 출력
print("%7.1f" % 123.45) # 소수점 아래 첫째 자리만 출력 , 소수점 아래 둘째자리에서 반올림
print("%7.3f" % 123.45) # 소수점 아래 셋째자리에서 출력, 오른쪽 빈칸은 0으로 채움

print("%s" % "Pyhon") # 자릿수만큼 출력
print("%10s" % "Python") # 오른쪽 정렬

print("%d %5d %05d" % (123,123,123))
print("{0:d} {1:5d} {2:05d}".format(123,123,123))
print("{2:d} {1:d} {0:d}".format(100,200,300))

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세개 출력")
print(r"\n \t \"\\를 그대로 출력")

a = int(input("당신의 나이는 몇살이세요?"))
print("제 나이는 %d 입니다." %a)
print("제 나이는 {0}입니다.".format(a))

name = input("당신의 이름은? ")
print("제 이름은 %s입니다." %name)

a = int(input("당신의 나이는 몇살이세요? "))
name = input("당신의 이름은? ")
print("제 나이는 %d이고, 이름은 %s 입니다." %(a,name))
print("제 나이는 {0}이고, 이름은 {1} 입니다.".format(a,name))
print(f"제 나이는 {a}이고, 이름은 {name} 입니다.")

# 문자열 개수 세기(count)
a = "hobby"
a.count('b')

# 위치 알려주기(find)
a = "Python is best choice"
a.find('b')
a.find('k') # 찾는 문자나 문자열이 없으면 -1로 반환된다.

# 위치 알려주기2(index)
a = "Life is too shoet"
a.index('t')
a.index('k') # 없는 문자일때 없다는 문구가 뜬다

# 문자열 삽입(join)
a = ","
a.join('abcd')

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
a.lower()

# 양쪽 공백 지우기(strip)
a = " hi "
a.strip()

# 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg")

# 문자열 나누기(split)
a = "Life is too short"
a.split() # 공백을 기준으로 문자열을 나눔
a = "a:b:v:d"
a.split(':')# :기호를 기준으로 문자열을 나눔

a = 5; b =3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

a,b,c = 2,3,4
print(a + b - c, a + b * c, a * b / c)

s1, s2 ,s3 = "100", "10.123", "99999999999999999999"
print(int(s1)+1, float(s2)+1, int(s3)+1)

a = 100 ;b = 10.123
str(a) + '1'
str(b) + '1'

a = 10
a += 5;print(a)
a -= 5;print(a)
a *= 5;print(a)
a /= 5;print(a)
a //= 5;print(a)
a %= 5;print(a)
a **= 5;print(a)

# 동전교환 프로그램 구현
### 변수 선언 부분 ###
money, c500, c100, c50, c10 = 0,0,0,0,0

### 메인코드 작성 ###
money = int(input("교환할 돈은 얼마입니까? "))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n500원짜리 ===> %d개" %c500)
print("100원짜리 ===> %d개" %c100)
print("50원짜리 ===> %d개" %c50)
print("10원짜리 ===> %d개" %c10)
print("바꾸지 못한 잔돈 ===> %d원 \n" %money)

# 동전교환 프로그램 구현2
### 변수 선언 부분 ###
money, m50000, m10000, m5000, m1000 = 0,0,0,0,0

### 메인코드 작성 ###
money = int(input("교환할 돈은 얼마입니까? "))

m50000 = money // 50000
money %= 50000

m10000 = money // 10000
money %= 10000

m5000 = money // 5000
money %= 5000

m1000 = money // 1000
money %= 1000

print("\n50000원짜리 ===> %d개" %m50000)
print("10000원짜리 ===> %d개" %m10000)
print("5000원짜리 ===> %d개" %m5000)
print("1000원짜리 ===> %d개" %m1000)
print("바꾸지 못한 잔돈 ===> %d원 \n" %money)

# 리스트 자료형
odd = [1, 3, 5, 7, 9]
a = [ ]
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'shot']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트의 인덱싱
a = [1, 2, 3]
a[0] 
a[0] + a[2]
a[-1]
a = [1, 2, 3, 4, 5]
a[0:2]
b = a[:2]
c = a[2:]
b
c

# 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
a + b

# 리스트 반복하기
a = [1, 2, 3]
a * 3

a = [1, 2, 3, ['a','b','c']]
a[0]
a[-1]
a[3][0]
a[3][-1]

a = [1, 2, ['a','b',['Life','is']]]
a[2][2][0]
a[-1][1]

# 리스트에서 하나의 값 수정하기
a = [1, 2, 3]
a[2] = 4
a
# 리스트에서 연속된 볌위의 값 수정하기
a[1:2] = ['a','b','c']
a

# [] 사용해 리스트 요소 삭제하기
a = [1, 'a', 'b', 'c', 4]
a[1:3] = []
a

# del 함수 사용해 리스트 요소 삭제하기
a = [1, 'a', 'b', 'c', 4]
del a[1]
a
# 슬라이싱 사용하여 한번에 삭제가능
a = [1,2,3,4,5]
del a[2:]
a

# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
a.append([7,8]) # 리스트 추가
a

# 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
a

# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
a

# 위치 반환(index)
a = [1, 2, 3]
a.index(3) # 3은 리스트 a의 세번째
a.index(1)
a.index(0) # 없는값은 에러메세지 출력

# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0,4) # a[0]위치에 삽입
a

# 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a

# 리스트 요소 끄집어내기(pop)
a = [1,2,3]
a.pop() # 맨 마지막 요소를 돌려 주고 그 요소는 삭제하는 함수
a

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
a.count(1) # 리스트 내에 1이 몇개 있는지

# 리스트 확장(extend)
a = [1, 2, 3]
a.extend([4,5])
a
b = [6, 7]
a.extend(b)
a

# 튜플 자료형 a = (1,2,3,) 변수 선언후 ()
# 튜플 요소값 삭제시 오류
t1 = (1, 2, 'a', 'b')
del t1[0]
# 튜플 요소값 변경시 오류
t1 = (1, 2, 'a', 'b')
t1[0] = 'c'

# 튜플은 인덱싱은 가능하다
t1 = (1, 2, 'a', 'b')
t1[0]
t1[3]
# 튜플은 슬라이싱은 가능하다.
t1 = (1, 2, 'a', 'b')
t1[1:]
# 더하기
t2 =(3,4)
t1 + t2
# 곱하기
t2 * 3
# 길이 구하기
len(t1)
