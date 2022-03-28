from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 해당사이트에서 검색 입력후 앤터기능을 하기위해



driver = webdriver.Chrome(executable_path= 'C:/Users/김윤섭/Downloads/chromedriver_win32/chromedriver')
driver.get("http://secure-retreat-92358.herokuapp.com/")

search = driver.find_element_by_name("fName")
search.send_keys("Kim")
search = driver.find_element_by_name("lName")
search.send_keys("Youn Sub")
search = driver.find_element_by_name("email")
search.send_keys("tldn0330@naver.com")
enter = driver.find_element_by_xpath('/html/body/form/button')
enter.click()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(chromedriver, options=options)