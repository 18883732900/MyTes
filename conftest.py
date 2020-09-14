import os
import time
import allure
import pytest
# 添加报错截图到allure报告里
from Base.Base_InitDriver.initdriver import inidriver

driver = None

'''
会自动监听用例断言结果针对失败的用例进行截图并加入报告
'''
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
            allure.attach('截图.png', jpg, allure.pytest_plugin.AttachmentType.PNG)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    out= yield
    rep = out.get_result()
    print(rep)
    print(out)
    print(rep.when)
    print(rep.nodeid)
    print(rep.outcome)




@pytest.fixture(scope = "class")
def conf_initdriver():
    global driver
    driver = inidriver('http://test.bjhontai.com:180/#/login')
    driver.maximize_window()
    yield driver
    time.sleep(3)
    driver.quit()
    del driver




if __name__ == '__main__':
   a=conf_initdriver()
