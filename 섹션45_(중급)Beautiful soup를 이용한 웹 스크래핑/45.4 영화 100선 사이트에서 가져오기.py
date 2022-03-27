from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")
print(soup.title)
all_movie = soup.find_all(name="h3", class_="97) Amelie") # 아니 강의에서는 class가 title로 나온는데
print(all_movie)

movie_title = [movie.getText() for movie in all_movie]
movies = movie_title[::-1] # 출력 순서를 바꿔준다 100번째부터 출력되는것을 1로
# article_text = []
# for title in article_tag:
#     text = title.getText()
#     article_text.append(text)
    
# print(article_text)

# 마지막 엑셀 테스트 파일로 변환하기 위해
with open ("movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")