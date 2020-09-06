from selenium import webdriver


def inidriver(url):
    '''
         选择浏览器
         选择添加访问链接
    '''
    driver = webdriver.Firefox()
    driver.get(url)
    return driver
