from selenium import webdriver


driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver')
driver.get("https://www.melon.com/chart/index.htm/")


bug_link = driver.find_elements_by_css_selector(".wrap a")
for song in bug_link:
    print(song.text)

driver.quit()

