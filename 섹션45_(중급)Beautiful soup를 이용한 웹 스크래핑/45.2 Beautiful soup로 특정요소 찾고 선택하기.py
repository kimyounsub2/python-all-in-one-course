from bs4 import BeautifulSoup


with open("섹션45_(중급)Beautiful soup를 이용한 웹 스크래핑\website.html",encoding ="UTF8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser") # 여기서 markup은 HTML의 M을 의미한다.


all_anchor_tags = soup.find_all(name="a") # 가장 많이 쓰이는 함수고 모든 a 태크를 불러올수 있다.
print(all_anchor_tags)