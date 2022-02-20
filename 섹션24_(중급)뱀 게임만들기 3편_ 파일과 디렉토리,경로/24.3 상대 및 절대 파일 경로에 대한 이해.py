
# my_file의 경로가 바탕화면에 있을경우 해당 파일의 경로를 /를 구분져서 입력해주면 된다.
with open("/Users/김윤섭/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)  
    
    
# Absolute 절대파일
# 절대 파일 경로는 항상 여러분의 컴퓨터에 있는 루트와 관련이 있다.

with open(".\Desktop\my_file.txt") as file:
    contents = file.read()
    print(contents)  
# Relative 상대파일
# 상대파일 경로는 현재 작업하고 잇는 디렉토리와 관련이 있다. 그래서 내가 어디에 있는지. 어디에 도달하고 싶은지에 달려있다.
