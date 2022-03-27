import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:/Users/김윤섭/Downloads/chromedriver_win32/chromedriver')
driver.get("https://www.empireonline.com/movies/features/best-movies-2/")
html = driver.page_source
soup = BeautifulSoup(html)
prodList = soup.find_all("h3", {"class": "jsx-4245974604"})
print(prodList)

movie_titles = [movie.getText() for movie in prodList]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding='UTF-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
