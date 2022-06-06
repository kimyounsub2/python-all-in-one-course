# 파일 생성하기
f = open("C:\doit\새파일.txt", 'w')
f.close()

# 파일을 쓰기 모드로 열어 출력값 적기
f = open("C:\doit\새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# readline() 함수
f = open("C:\doit\새파일.txt", 'r')
line = f.readline() 
print(line)
f.close()

f = open("C:\doit\새파일.txt", 'r')
while True:
    line = f.readline() 
    if not line: break
    print(line)
f.close()

f = open("C:\doit\새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip() # 줄 바꿈 삭제 : 한칸 안띄우고 실행
    print(line)
f.close()

# read() 함수 이용하기
f = open("C:\doit\새파일.txt", 'r')
data = f.read() # 파일의 전체 내용을 리스트로 문자열로 반환한다.
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open("C:\doit\새파일.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함께 사용하기
f = open("C:/doit/foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("C:/doit/foo1.txt",'w') as f:
    f.write("Life is too short, you need python")

# 예제 1
f = open("C:/doit/dream1.txt", 'r')
contents = f.read()
print(contents)
f.close()

with open("C:/doit/dream1.txt", 'r') as f:
    content1 = f.read()
print(content1)

# 파일 글자의 통계 정보 출력하기
with open("C:/doit/dream1.txt", 'r') as my_file:
    contents = my_file.read()
    word_list = contents.split(" ") # 빈칸기준으로 단어를 분리 리스트
    line_list = contents.split("\n")# 한 줄씩 분리하여 리스트
    
print("총 글자의 수:", len(contents))
print("총 단어의 수:", len(word_list))
print("총 줄의 수:", len(line_list))
