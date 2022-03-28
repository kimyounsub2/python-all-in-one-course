from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 해당사이트에서 검색 입력후 앤터기능을 하기위해

driver = webdriver.Chrome(executable_path= 'C:/Users/김윤섭/Downloads/chromedriver_win32/chromedriver')
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cokies = driver.find_element_by_id("cookie")
cokies.click()