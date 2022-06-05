# 누적 합계가 1000 이상이 되는 시작 지점 알기
hap, i = 0,0
for i in range(1,101):
    hap += i
    print("i값은 = %d hap = %d"%(i, hap))
    if hap >= 1000:
        break
print("1~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d"%i)

# 1 ~ 100의 합계를 구하되, 3의 배수 제외하고 더하기
hap, i = 0,0
for i in range(1, 101):
    if i % 3 == 0:
        continue
    hap += i
    print("i=%d hap=%d" %(i, hap))
print("1~100의 합계(3의 배수 제외) : %d"%hap)

# 1부터 1000 까지의 홀수의 합계 중에서, 최초로 1000이 넘는 숫자는 어떤 것인지 구하는 프로그램을 작성해 보세요.
hap, i = 0,0
for i in range(1,1001,2):
    hap += i
    if hap >= 1000:
        break
print(hap,i)

# numbers = [55, 5, 15, 6, 20, 7, 25, 43] 일 때 결과가

55
15
20
25
43

# 출력 되도록 하세요.
numbers = [55, 5, 15, 6, 20, 7, 25, 43]
for i in numbers:
    if i < 10:
        continue
    print(i)

# 리스트 기본 활용
aa = []
for i in range(0,4):
    aa.append(0)
hap = 0

for i in range(0,4):
    aa[i] = int(input(str(i + 1) + "번째 숫자:"))
hap = aa[0] + aa[1] +aa[2] + aa[3]
print("합계 ==> %d" % hap)

# 리스트 기본
aa = []
bb = []
value = 0
for i in range(0, 100):
    aa.append(value)
    value += 2
print("aa[0]에는 %d이, aa[99]에는 %d이 입력됩니다."%(aa[0],aa[99]))
for i in range(0, 100):
    bb.append(aa[99 - i])
print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다."%(bb[0],bb[99]))

# 리스트 함수 정리
myList = [30, 10, 20]
print("현재 리스트 : %s" %myList)

myList.append(40)
print("append(40) 후의 리스트 : %s" %myList)

print("pop()으로 추출한 값 : %s" %myList.pop())
print("pop() 후의 리스트 : %s" %myList)

myList.sort()
print("sort() 후의 리스트 : %s" %myList)

myList.reverse()
print("reverse() 후의 리스트 : %s" %myList)

print("20값의 위치 : %d" %myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s" %myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s" %myList)

myList.extend([77,88,77])
print("extend([77,88,77]) 후의 리스트 : %s" %myList)

print("77값의 개수 : %d" %myList.count(77))

# 딕셔너리를 활용해 음식 궁합을 출력하는 프로그램
foods = {"떡볶이" : "오뎅",
         "짜장면" : "단무지",
         "라면" : "김치",
         "피자" : "피클",
         "맥주" : "땅콩",
         "치킨" : "치킨무",
         "삼겹살" : "상추"};
         
while(True):
    myfood = input(str(list(foods.keys())) + " 중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s> 궁합 음식은 <%s> 입니다." %(myfood,foods.get(myfood)))
    elif myfood == "끝":
        break
    else:
        print("그런 음식이 없습니다. 확인해보세요.")



