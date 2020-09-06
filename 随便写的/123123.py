import time

from selenium import webdriver

driver=webdriver.Firefox()
driver.get('http://a.bjhontai.com')
driver.maximize_window()
time.sleep(10)
el=driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[1]/div/div/input')
print(el)

el.send_keys('admin')