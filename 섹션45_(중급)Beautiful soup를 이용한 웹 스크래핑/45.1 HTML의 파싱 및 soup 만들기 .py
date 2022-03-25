from bs4 import BeautifulSoup


with open("섹션45_(중급)Beautiful soup를 이용한 웹 스크래핑\website.html",encoding ="UTF8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser") # 여기서 markup은 HTML의 M을 의미한다.
print(soup.title) # 해당요소만 가져올수 있지만
print(soup.title.string)
print(soup) # 이렇게 전체를 출력할수도 있다.