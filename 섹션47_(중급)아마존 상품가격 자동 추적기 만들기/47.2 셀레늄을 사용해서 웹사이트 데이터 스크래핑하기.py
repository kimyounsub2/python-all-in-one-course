from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver')
driver.get("https://www.python.org/")

event_time = driver.find_elements_by_css_selector(".event-widget time")
event_new = driver.find_elements_by_css_selector(".event-widget li a")
events = {}
for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_new[n].text,
    }   

print(events)