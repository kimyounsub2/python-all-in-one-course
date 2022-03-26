from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
#print(soup.title) # 사이트의 제목을 알려면 

###### 이사이트의 단 하나씩만 조회할때 사용
article_tag = soup.find(name = "a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()
# print(article_tag)
# print(article_text)
# print(article_link)
# print(article_upvote)


##### 이싸이트의 전체 조회할때
articles = soup.find_all(name = "a", class_="titlelink")
article_text1 = []
article_link1 = []
for article_tag1 in articles:
    text = article_tag1.getText()
    article_text1.append(text)
    link = article_tag1.get("href")
    article_link1.append(link)

article_upvote1 = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_text1)
# print(article_link1)
print(article_upvote1)
    
largest_number = max(article_upvote1) # 투표율 최대치 조히
largest_index = article_upvote1.index(largest_number) # 투표율 최대치가 몇번째에 있는지
print(article_text1[largest_index])
print(article_link1[largest_index])