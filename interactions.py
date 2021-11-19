from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/omarmahmoud/Downloads/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')

is_on= True
times = 1500
for i in range(5):

    cookie = driver.find_element_by_id('bigCookie')
    times += 5000
    for i in range(times):
        cookie.click()

    for num in range(4, 0, -1):
        print(num)
        money = int(driver.find_element_by_id('cookies').text.replace(',', '').split()[0])
        prize = driver.find_element_by_id(f'productPrice{num}').text
        prize = prize.replace(',', '')
        if prize.isnumeric():
            prize = int(prize)
            if prize < money:
                prize=driver.find_element_by_id(f'product{num}')
                prize.click()
        else:
            pass

per_sec= driver.find_elements_by_id('cookies')[1]
print(per_sec)
#driver.quit()
