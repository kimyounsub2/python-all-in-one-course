########################## 단 텍스트를 불러올때 폴더안의 txt를 불러올수 없고 전체경로를 불러올수있다.
# my_file.txt에 있는 내용을 불러올수 있다.
# file = open("my_file.txt")
# # 다음으로 파일을 읽는다.
# # read 메소드는 파일의 컨텐츠를 문자열로 변환해 준다. 
# # 지금 변수 contents에 그 내용을 저장하고 contents를 출력한다.
# contents = file.read()
# print(contents)
# file.close() # 파일을 open을 했으면 close를 해줘야 한다.
# 왜 파일을 오픈하고 닫아야 하나 -- 파이썬이 파일을 열면, 기본적으로 컴퓨터의 자원을 차지하게 된다.
# 그리고 나중에 파일을 닫아서 그 리소스들을 해방시키기로 결정할수도 있다. 
# 하지만 언제 일어날지와 일어날지 열부도 알수없다. 그래서 대신에 수동적으로 파일을 닫아야 한다.

# my_file.txt에 있는 내용을 불러올수 있다.
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)   
# with를 사용하면 더이상 파일닫을 필요가 없다.
# with 키워드는 파일을 직접 관리할 것이다. 우리가 일을 끝냈다는 것을 알아채는 즉시, 파일을 닫을 것이다.

with open("new_file.txt", mode = "w") as file: 
    file.write("\nNew text.")
# mode = r 기본적으로 읽기 전용으로 설정된다.
# mode = w 편집가능하게 만든다.
# mode =a 는 append를 사용해서 새 텍스트를 쓸수 있고 새줄을 추가할수 있다.
    
