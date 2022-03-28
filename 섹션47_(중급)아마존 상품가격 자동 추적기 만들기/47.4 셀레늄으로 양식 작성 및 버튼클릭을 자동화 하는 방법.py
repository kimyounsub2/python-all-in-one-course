from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 해당사이트에서 검색 입력후 앤터기능을 하기위해

driver = webdriver.Chrome(executable_path= 'C:/Users/김윤섭/Downloads/chromedriver_win32/chromedriver')
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# votes = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(votes.text)
article_count = driver.find_element_by_css_selector("#articlecount a")
#article_count.click() # 해당링크를 클릭해주는 기능이다.

all_portals = driver.find_element_by_link_text("All portals") 
# all_portals.click() 해당 사이트의 All portals를 클릭한다.

search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
