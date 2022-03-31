import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver')
driver.get("https://www.melon.com/chart/index.htm")
html = driver.page_source
soup = BeautifulSoup(html)
prodList = soup.find_all("a")
print(prodList)