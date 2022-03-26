from bs4 import BeautifulSoup


with open("섹션45_(중급)Beautiful soup를 이용한 웹 스크래핑\website.html",encoding ="UTF8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser") # 여기서 markup은 HTML의 M을 의미한다.


all_anchor_tags = soup.find_all(name="a") # find_all은 가장 많이 쓰이는 함수고 속성을 기준으로 항목을 검색할수 있다
print(all_anchor_tags)

for tag in all_anchor_tags: # 택스트 식으로 정렬하여 출력할수 있다
    # print(tag.getText()) 하지만 이렇게만 하면 링크까지 끌고 올수 없다.
    print(tag.get("href")) # 사이트의 링크도 출력할수 있다.
    
    
heading = soup.find(name="h1",id="name") # 따라서 해당특정 요소를 가져올수 있다
print(heading) # 하나의 h1만 가져온 것을 확인할 수 있다

section_heading = soup.find(name="h3", class_="heading") # 일반적으로 파이썬은 class라는 예약함수가 따로 존재하기 때문에 html에서 class를 가져오기 위해선 class_붙여서 사용한다.
print(section_heading)

# select은 일치하는 모든항목을 리스트로 가져온다
# select_one은 처음으로 일치하는 항목을 가져온다
name = soup.select_one(selector="#name") 
print(name)

heading = soup.select(".heading")
print(heading)