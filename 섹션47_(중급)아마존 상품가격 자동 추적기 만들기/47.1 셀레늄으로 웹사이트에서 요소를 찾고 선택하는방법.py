from selenium import webdriver


# driver = webdriver.Chrome(executable_path= 'C:/Users/김윤섭/Downloads/chromedriver_win32/chromedriver')
# driver.get("https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904&th=1")
# price = driver.find_element_by_id("acrCustomerReviewText")
# print(price.text) # 아마존 사이트에서 해당 id 출력하기

############ 파이썬 사이트에서 여러가지 메소드 사용해서 출력하기

driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver')
driver.get("https://www.python.org/")
# name으로 해당 요소 찾기
# search_bar = driver.find_element_by_name("q")
# print(search_bar)

logo = driver.find_elements_by_class_name("python-logo")

# Xpath는 경로 구조로 특정 HTML 요소의 위치를 찾는 방법이다.
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)
driver.quit()

# element 는 조건에 일치하는 가장 첫번째 요소를 반환
# elements는 조건에 일치하는 모든 요소를 list 형태로 반환
# 즉, 한개만 return하냐, 모든 요소를 return 하냐의 차이다.

