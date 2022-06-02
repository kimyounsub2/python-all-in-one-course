
# 리스트의 필요성
# 예제 1 : 변수를 a,b,c,d로 4개로 만들었을때
a,b,c,d = 0,0,0,0
hap = 0

a = int(input("1번째 숫자 : "))
b = int(input("2번째 숫자 : "))
c = int(input("3번째 숫자 : "))
d = int(input("4번째 숫자 : "))

hap = a + b + c + d
print("합계 ==> %d" %hap)
# 예제 2 : 변수를 aa하나로 리스트로 만들었을때
aa = [0,0,0,0]
hap = 0

aa[0] = int(input("1번째 숫자 : "))
aa[1] = int(input("2번째 숫자 : "))
aa[2] = int(input("3번째 숫자 : "))
aa[3] = int(input("4번째 숫자 : "))

hap = aa[0] + aa[1] + aa[2] + aa[3]
print("합계 ==> %d" %hap)

# 예제 3 : for문 사용하여 만들기
aa = []
for i in range(0,4):
    aa.append(0)
hap = 0

for i in range(0,4):
    aa[i] = int(input(str(i +1) + "번째 숫자: "))
    
for i in range(0,4):
    hap += aa[i]

# hap = aa[0] + aa[1] + aa[2] + aa[3]
print("합계 ==> %d" %hap)
    
# 딕셔너리 자료형
dic = {'name':'pey',
       'phone':'0119993323',
       'birth' : '1118'}

# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'
a['name'] = 'pey' 
a[3] = [1,2,3]
a

# 딕셔너리 요소 삭제하기
del a[1]
del a['name']
a

# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey' : 10, 'julliet': 99}
grade['pey']
grade['julliet']
# 딕셔너리 만들때 주의할 사항
a = {1:'a', 1:'b'} # 중복된 키 값을 사용할수 없다.
a

# Key 리스트 만들기(keys), Value 리스트 만들기(values)
a = {'name':'pey', 'phone':'0119993323', 'birth' : '1118'}
a.keys() # key 값만 출력된다
a.values() # values값만 출력된다.

for i in a.keys():
    print(i)
    
for i in a.values():
    print(i)

# Key, Value 쌍 얻기(items)
a = {'name':'pey', 'phone':'0119993323', 'birth' : '1118'}
a.items()

# Key: Value 쌍 모두 지우기(clear)
a.clear()
a

# Key호 Value 얻기(get)
a.get('name')
a.get('phone')

# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
'name' in a # 안에 있으면 True
'email' in a # 안에 없으면 False

# 집합(set) 자료형
s1 = set([1,2,3])
s1
# 순서가 없고 중복이 허용되지 않는다.
s2 = set("Hello")
s2 # l이 중복되어 하나만 출력된다

# 교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s1 & s2 # 방법 1
s1.intersection(s2) # 방법 2

# 합칩합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s1 | s2 # 방법 1
s1.union(s2) # 방법 2

# 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
# 방법 1
s1 - s2
s2 - s1
# 방법 2
s1.difference(s2)
s2.difference(s1)

# set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한후 해야한다.
s1 = set([1,2,3])
l1 = list(s1)
l1
l1[0]

t1 = tuple(s1)
t1
t1[0]

# 집합자료형 값 1개 추가하기(add)
s1 = set([1,2,3])
s1.add(4)
s1
# 값 여러 개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
s1
# 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
s1

# 자료형의 참과 거짓은 어떻게 사용되나?
ab = [1,2,3,4]
while ab:
    print(ab.pop())
type(ab)

a = True
b = False
type(a)

# a 리스트에서 중복된 숫자들을 제거해 보세요
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
aSet
b = list(aSet)
print(b)

# 자료형의 값을 저장하는 공간,변수
# 리스트 변수 주의사항
a = [1,2,3]
b = a
a[1] = 4

# 변수를 같이 하여 나중에도 같게 변한다.
print(a)
print(b)
print(id(a)) # 아이디 주소가 같다
print(id(b)) # 아이디 주소가 같다
a is b
# 값이 변경되지 않게 하려면 스라이싱으로 복사
a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)
a is b
from copy import copy
a = [1,2,3]
b = copy(a)
a[1] = 4
print(a)
print(b)
a is b
