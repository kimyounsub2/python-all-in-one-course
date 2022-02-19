# my_file.txt에 있는 내용을 불러올수 있다.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    
# with를 사용하면 더이상 파일닫을 필요가 없다.
# with 키워드는 파일을 직접 관리할 것이다. 우리가 일을 끝냈다는 것을 알아채는 즉시, 파일을 닫을 것이다.

# mode = r 기본적으로 읽기 전용으로 설정된다.
# mode = w 편집가능하게 만든다.
# mode =a 는 append를 사용해서 새 텍스트를 쓸수 있고 새줄을 추가할수 있다.
with open("new_file.txt", mode = "w") as file: 
    file.write("New text.")