from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:/Users/김윤섭/Downloads/chromedriver_win32/chromedriver')
driver.get("https://en.wikipedia.org/wiki/Main_Page")

votes = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(votes.text)
article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)