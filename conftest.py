import os
import allure
from selenium import webdriver
import pytest

# 添加报错截图到allure报告里
from Base.initdriver import inidriver

driver = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # 我们只看错误的用例，不包括setup和teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # 访问一个固定装置
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # pic_info = adb_screen_shot()
        with allure.step('添加失败截图...'):
            jpg = driver.get_screenshot_as_png()
            allure.attach('参数.png', jpg, allure.pytest_plugin.AttachmentType.PNG)




@pytest.fixture(scope='session')
def browser():
    global driver
    if driver is None:
        driver = inidriver('http://172.16.13.105/#/login')
        driver.maximize_window()
    return driver
