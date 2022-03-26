answer = input("음악 여행을 몇 년도로 갈것입니까? 입력은 YYYY-MM-DD 형식으로 받습니다") 
print(answer)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.billboard.com/charts/hot-100/2022-03-26/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
print(soup.title)

all_song = soup.find_all(name="h3", id="title-of-a-story")
song_title = [movie.getText() for movie in all_song]
print(song_title)

