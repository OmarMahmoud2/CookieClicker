from selenium import webdriver


chrome_driver_path = "/Users/omarmahmoud/Python/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

dates= driver.find_elements_by_css_selector('.event-widget time')
names= driver.find_elements_by_css_selector('.event-widget li a')
events={}

for num in range(5):
    events[num] = {dates[num].text:names[num].text}


print(events)

driver.quit()

