# 내장함수
abs(3) # 어떤 숫자를 입력받았을 때, 그숫자의 절댓값을 돌려주는 함수

# All : 모두가 참인지 검사
all([1,2,3]) # True
all([1,2,3,0]) #0은 거짓이라서 False

# any : 하나라도 참이 있을 경우 True를 리턴
any([1, 2, 3, 0]) # 1,2,3이 참이라서 T
any([0, ""]) # 두개 요소 모두 거짓임으로 F

# chr : 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
chr(97)

# dir : 자체적으로 가지고 있는 변수나 함수를 보여준다.
dir([1,2,3])
dir({'1':'a'})

# divmod : 몫과 나머지를 튜플 형태로
divmod(7,3)

# emumerate : For문처럼 반복되는 구간에서 객체가 현제 어느 위치에 있는지 알려주는 인덱스 값이 필요할때
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
    
# eval : 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과를 리턴한다.
eval('1+2')
eval("'hi' +'a'")
eval('divmod(4,3)')

# filter : 무엇인가를 걸러낸다는 뜻 
# positive : 리스트를 입력값으로 받아 각각의 요소를 판별해서 양수 값만 돌려주는 함수
def positive(x):
    return x > 0
print(list(filter(positive, [1,-3,2,0,-5,6])))

# lambda 인자 : 표현식
print(list(filter(lambda x : x > 0, [1,-3,2,0,-5,6])))

# hex : 정수값을 입력받아 16진수로 변환하여 돌려주는 함수
hex(234)
hex(3)

# id : 객체를 입력받아 객체의 고유 주소 값을 돌려주는 함수
a = 3
id(3)

# input : 사용자 입력을 받는 함수
a = input()

# int : 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
int('3')

# isinstance : 첫번째 인수로 인스턴스, 두번째 인수로 클래스 이름을 받는다. 
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다
class Person: pass # 아무 기능이 없는 Person클래스 생성
a = Person() #Person 클래스의 인스턴스 a 생성
isinstance(a, Person) # a가 Person 클래스의 인스턴스인지 확인

# zip : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
list(zip([1, 2, 3], [4, 5, 6]))
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
list(zip("abc", "def"))
