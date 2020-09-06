from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
url = 'http://www.baidu.com'
driver.get(url)
el = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element(By.ID, 'kw'))
el.send_keys("周俊境")
el2 = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element(By.LINK_TEXT, '设置'))
el3 = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element(By.ID, 'su'))
ActionChains(driver).move_to_element(el2).click(el3).perform()
# el4=WebDriverWait(driver,5,0.5).until(lambda x:x.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]'))
# print(el4.text)
el.send_keys(Keys.CONTROL, 'a')
el.send_keys(Keys.CONTROL, 'x')
WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element(By.LINK_TEXT, '登录')).click()
WebDriverWait(driver, 10, 0.5).until(
    lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/div/div/div/div/div[4]/p[2]')).click()
WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element(By.ID, 'TANGRAM__PSP_11__userName')).send_keys(
    '18883732900')
el5 = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element(By.ID, 'TANGRAM__PSP_11__password'))
el5.send_keys('zjj5201314')
source = driver.page_source
print(type(source))
with open('./zhou.txt','wb',) as f:
    f.write(source.encode())
c=driver.get_screenshot_as_png()
with open ('./zjj.jpg','wb') as f:
    f.write(c)
