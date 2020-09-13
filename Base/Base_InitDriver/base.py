from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    __addr=None

    def __init__(self, driver):
        self.driver = driver

    def __new__(cls, *args, **kwargs):
        if cls.__addr==None:
            cls.__addr=object.__new__(cls)
        return cls.__addr

    def windows_handles(self):
        '''查看句柄'''
        handles = self.driver.window_handles
        return handles

    def switch_windows_handles(self, index):
        '''切换窗口'''
        handles = self.windows_handles()
        self.driver.switch_to.window(handles(index))

    def swicth_frame(self, type_text, swicth_frame_type=None, time=10, Frequency=0.5):
        '''进入表单'''
        le = self.find_element(type_text, time, Frequency)
        self.driver.switch_to.frame(le)

        if swicth_frame_type == "parent_frame":
            '''进入上级表单'''
            self.driver.switch_to.parent_frame()
        elif swicth_frame_type == "default_content":
            '''进入顶层表单'''
            self.driver.switch_to.default_content()

    def swicth_alert(self, alert_type=None):
        '''进入警告弹窗'''
        f = self.driver.switch_to.alert

        if alert_type == 'accept':
            '''通过警告弹窗'''
            f.accept()

        elif alert_type == 'dismiss':
            '''退出弹窗'''
            f.dismiss()

    def select(self):
        self.select()

    def for_find_OP(self,el,p=None,type='click',text=None):
        els=self.find_elements(el)
        for i in els:
          if p in i.text :
             if type=='click':
                i.click()
             if type=='send_keys':
                 i.send_keys(text)
             break



    def page(self, fun, x=None, y=None, filepath=None):
        '''最大化窗口'''
        if fun == 'maximize_window':
            self.driver.maximize_window()

        '''刷新页面'''
        if fun == 'refresh':
            self.driver.refresh()

        '''回退到下个页面⬅'''
        if fun == 'back':
            self.driver.back()

        '''前进到上个页面➡'''
        if fun == 'forward':
            self.driver.forward()

        '''设置窗口尺寸'''
        if fun == 'set_window_size':
            self.driver.set_window_size(x, y)

        '''设置窗口在电脑屏幕上的位置'''
        if fun == 'set_window_position':
            self.driver.set_window_position(x, y)

        '''获取当前页面的url'''
        if fun == 'driver.current_url':
            url = self.driver.current_url
            print(url)
            return url

        '''获取当前页面的网页源代码'''
        if fun == 'driver.page_source':
            source = self.driver.page_source
            # if filepath is not filepath:
            #     with open(filepath, 'wb') as f:
            #         f.write(source.encode())
            return source

        '''获取当前页面的截图'''
        if fun == 'get_screenshot_as_png':
            jpg = self.driver.get_screenshot_as_png()
            return jpg
            # with open(filepath, 'wb') as f:
            #     f.write(jpg)
        '''获取当前页面的截图'''
        if fun == 'get_screenshot_as_file':
            self.driver.get_screenshot_as_file(filepath)

    '''显示等待定位元素'''

    def find_element(self, type_text, time=10, Frequency=0.5):
        el = WebDriverWait(self.driver, time, Frequency).until(lambda x: x.find_element(*type_text))
        return el

    '''显示等待定位元素组'''

    def find_elements(self, type_text, time=10, Frequency=0.5):
        el = WebDriverWait(self.driver, time, Frequency).until(lambda x: x.find_elements(*type_text))
        return el

    '''操作'''

    def Operation(self, type_text, op, text=None, keys=None, time=10, Frequency=0.5):
        el = self.find_element(type_text, time, Frequency)
        action = ActionChains(self.driver)
        if op == 'click':
            '''点击'''
            el.click()

        elif op == 'send_keys':
            '''输入'''
            el.send_keys(text)

        elif op == 'keys':
            """模拟键盘操作"""
            el.send_keys(*keys)

        elif op == 'click_and_hold':
            '''保持点击状态不松开'''
            action.click_and_hold(el).perform()

        elif op == 'double_click':
            '''双击'''
            action.double_click(el).perform()

        elif op == 'move_to_element':
            '''鼠标悬停'''
            action.move_to_element(el).perform()


        elif op == 'context_click':
            '''右键点击'''
            action.context_click(el).perform()

    def Javascript(self, x, y=None):
        '''滚动操作'''
        if y == None:
            js = 'var q=document.documentElement.scrollTop=%s' % x
            self.driver.execute_script(js)
        else:
            for i in range(y):
                js = 'window.scrollTo(0,%d)' % (i * x)
                self.driver.execute_script(js)
                sleep(0.5)

    def implicitly_wait(self, time):
        self.driver.implicitly_wait(time)

    def selects(self, type, type_text, value=None, time=5, Frequency=0.5):
        el = self.find_element(type_text, time, Frequency)
        se = Select(el)
        if type == 'all':
            '''返回所有已选项'''
            return se.all_selected_options

        elif type == 'first':
            '''返回第一个已选项'''
            return se.first_selected_option

        elif type == 'options':
            '''返回所有选项'''
            return se.options

        elif type == 'is_multiple':
            '''
            返回是否为多选
            True:多选
            Flase：不多选  
            '''
            return Select(el).is_multiple

        elif type == 'index':
            '''按照序号选择选项 从0开始'''
            Select(el).select_by_index(value)

        elif type == 'value':
            '''已这个下拉菜单选项的option的标签中的任意属性值进行查找'''
            Select(el).select_by_value(value)

        elif type == 'visible_text':
            '''按照选项值进行查找'''
            Select(el).select_by_visible_text(value)

    # def __del__(self):
    #     sleep(10)
    #     try:
    #         self.driver.quit()
    #
    #     except:
    #         print('异常关闭')
