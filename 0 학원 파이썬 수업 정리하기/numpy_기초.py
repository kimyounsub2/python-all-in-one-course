import numpy as np
#%% 1처 list->array
list1 = [1,2,3,4]
# 넘파이 배열로 변환
# 반복문을 작성할 필요가 없다
a = np.array(list1)
print(a+1)
print(a.shape) # 배열구조(크기)
print(a.ndim) # 차원수
print(a.size) # 배열요소 개수
print(a.dtype) # 요소자료형

# 리스트 float형으로 변환후 넘파이 배열로 변환
np.array([float() for i in list1])
# 넘파이 배열을 float형으로 변환
a.astype(float)
np.array(list1,dtype=float)
# list에서 array간 변호나속도가 빠르다
np.fromiter(list1,dtype=float)
np.insert(a,3,10000000000)
# 정수32비트 int32,np.int,np.int32 동일
# 정수64비트 np.int64
a2 = np.array(list1, dtype=np.int64)
np.insert(a2,3,10000000000)
# 일차원경우 배열요소 개수
len(a)
type(a)
#%% 2차 list->array
b = np.array([[1,2,3],[4,5,6]])
print(b.shape) # 배열구조(크기)
print(b.ndim) # 차원수
print(b.size) # 배열요소 개수
print(b.dtype) # 요소자료형

# 이차원경우 행수 shape의 첫번째 요소
len(b)
type(b)

#%% array->list
a.tolist()
b.tolist()

#%% 또다른 넘파이 배열 만들기
np.zeros((2,))
np.zeros((2,2))

zero = [[0,0],[0,0]]
np.array(zero,dtype=float)

# 중첩 for
# 2행 2열
lst1=[]
lst2=[]
for i in range(2): # 행 개수
    for j in range(2): # 열 개수
        lst1.append(0) # 한 개의 행
    lst2.append(lst1)
    lst1=[]
np.array(lst2)

# [[range(열개수)] range(행개수)]
lst2 = [[0 for i in range(2)] for j in range(2)]
np.array(lst2)

np.ones((2,2))
np.full((2,2),5)
np.eye(2)

#%% 배열크기구조 변경
np.array(range(20)).reshape(4,5)

a = np.array(range(20))
# 20의 약수를 지정
a.reshape(4,5)
a.reshape(-1,5)
a.reshape(4,-1)


# 2차 배열을 1차배열로 변환
a = np.array(range(20))
b = a.reshape(4,5)
b.reshape(a.size)
b.reshape(a.size,)
b.reshape(-1)
b.reshape(-1,)
b.flatten()

#%% 1차 리스트 인덱싱, 슬라이싱
arr = np.array(range(20))
arr
arr[0]
arr[-1]
arr[[0,1,2]]
arr[0:3]
# 확장 슬라이스
# [::인덱스증감치(step, 간격)]
arr[0:3:1]
arr[0:3:2]
arr[0:9:2]
arr[::-1] # 역 정렬

#%% 2차 배열 인덱싱,슬라이스
lst = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
arr = np.array(lst)
# 행인덱스만 적용
arr[0]
arr[-1]
arr[[0,1,2]]
arr[0:3]
arr[0:3:1]
arr[0:3:2]

arr[0][0]
arr[0:3][0]

# 행인덱스와 열인덱스를 동시 적용
arr[0:2,0:2]

# 특정 열의 모든행
arr[ : ,2]
# 특정 2행의 모든열
arr[2, : ]
arr[2]

# 마지막열
arr[:, -1]

# 마지막 행
arr[-1:,:]
arr[0:3:2,0:3:2]
arr[:]
arr[::]
arr[::-1] # 역정렬
arr[::-1,::-1] # 역정렬

# (0행,1행)의 (0열 1열)
# arr[0:2, 0:2]로 해석하지 말고 
# 0행0열, 1행1열 요소라고 해석하자
arr[[0,1],[0,1]]
# 다중인덱스와 슬라이스를 조합
arr[0:2,[0,1]]

#%% 조건에 만족하는
import numpy as np
lst = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
a = np.array(lst)
bool_indexing_array = np.array([
[False, True, False],
[True, False, True],
[False, True, False]
])
n = a[bool_indexing_array]
n = a[a%2==0]
n = a[a%2==1]
print(n)

# 3보다 큰 요소
n = a[a>3]
print(n)

# 6보다 작은 요소
a[a<6]

# 3보다 크고 6보다 작은 요소
a[(a >3) & (a<6)]

# 3 혹은 6 요소
a[(a==3) | (a==6)]

#%% 조건에 만족하는 요소의 인덱스 배열 리턴
a[a > 3]
# array([4, 5, 6, 7, 8, 9])
np.where(a >3)
# (array([1, 1, 1, 2, 2, 2], dtype=int64),
# array([0, 1, 2, 0, 1, 2], dtype=int64))
a
# 인덱스 리스트
list(zip(np.where(a >3)[0],np.where(a >3)[1]))

#%% 배열 혹은 리스트간 추가 통합,배열 삽입, 수정,삭제
# 1차배열
lst1=[1,2,3]
lst2=[4,5,7]

arr1 = np.array(lst1)
arr2 = np.array(lst2)

# 배열 혹은 리스트가 추가 통합된 1차배열
np.append(arr1,lst2)
np.append(lst1,arr2)
np.append(arr1,arr2)

# 배열 혹은 리스트가 삽입 통합된 1차배열
np.insert(arr1, 2,4)
np.insert(arr1, 2,[4,5])

# 수정
# 배열 자신에 반영
# 1번 인덱스의 값을 9로 수정
arr[1] = 9
arr1[0:2] = 9
arr1[arr1 > 2] = 9
arr1

arr1 = np.array(lst1)
# 조건식이 차이면 9로 수정 거짓이면 원 값으로 수정된 새 배열을 리턴
np.where(arr1 > 2,9,arr1)
arr1

# 삭제
# 1번 인덱스 요소 삭제
np.delete(arr1,1)
# 1번 2번 인덱스 요소 삭제
np.delete(arr1,[1,2])

# 2차배열 CUD
lst1=[1,2,3,3]
lst2=[4,5,7,7]

arr1 =np.array(lst1).reshape(2,-1)
arr2 =np.array(lst2).reshape(-1,2)

# 통합된 1차 배열 반환
np.append(arr1,arr2)

# 2차배열 배열차원 크기가 유지 통합
# 행(1행,2행순으로 세로)방향으로 추가 통합
np.append(arr1,arr2,axis=0)
# 열(1열,2열순으로 가로)방향으로 추가 통합
np.append(arr1,arr2,axis=1)

# 삽입
# 통합된 1차배열 반환
# array([1, 2, 2, 2, 3, 3])
np.insert(arr1,1,[2,2])
# [2,2]행을 행방향으로 1번 자리에 삽입
np.insert(arr1,1,[2,2],axis=0)
# [2,2]열을 열방향으로 1번 자리에 삽입
np.insert(arr1,1,[2,2],axis=1)

# 수정
arr1[0,:] =3
arr1[arr1 > 2] = 9
# 조건식이 참이면 1로 수정 거짓이면 원 값으로 수정된 새배열을 리턴
np.where(arr1 > 2,1,arr1)
arr1

# 삭제
lst1 =[1,2,3,3]
arr1 = np.array(lst1).reshape(2,-1)
# 1번 인덱스 요소 삭제
np.delete(arr1,1)
# 행(세로)방향의 1번 인덱스인 행 하나 삭제
np.delete(arr1, 1, axis=0)
# 1번 열 삭제
np.delete(arr1, axis=1)