import time

from selenium.webdriver.common.by import By

from Base.Base_InitDriver.base import Base
from Base.Base_InitDriver.initdriver import inidriver
from Common import Resident_check_in_data
from MYSQL.Mysqldb_test import Mysqldb_test

Common = Resident_check_in_data()


class Resident_check(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, name=None, password=None):
        self.find_element(Common.user_name[0]).clear()
        self.find_element(Common.user_password[0]).clear()
        self.Operation(*Common.user_name, name)
        self.Operation(*Common.user_password, password)
        self.Operation(*Common.login)
        time.sleep(3)

    def int(self, parent_Community, Community, Floor, unit, FL, roomId):
        self.for_find_OP(Common.element1, '人房信息', 'click')
        self.for_find_OP(Common.element2, '居民信息管理', 'click')
        self.for_find_OP(Common.element3, '居民入住登记', 'click')
        time.sleep(3)
        self.Operation(*Common.element4)
        self.for_find_OP(Common.element5, parent_Community, 'click')
        self.Operation(*Common.element6)
        self.for_find_OP(Common.element7, Community, 'click')
        self.Operation(*Common.element8)
        self.for_find_OP(Common.element9, Floor, 'click')
        self.Operation(*Common.element10)
        self.for_find_OP(Common.element11, unit, 'click')
        self.Operation(*Common.element12)
        self.for_find_OP(Common.element13, FL, 'click')
        self.for_find_OP(Common.element14, roomId, 'click')

    def submin(self):
        self.Operation(*Common.element15)

    def owner(self, name, idcard, number, num):
        time.sleep(3)
        self.find_element(Common.element16[0]).clear()
        self.Operation(*Common.element16, name)
        self.find_element(Common.element17[0]).clear()
        self.Operation(*Common.element17, idcard)
        self.find_element(Common.element18[0]).clear()
        self.Operation(*Common.element18, number)
        self.find_element(Common.element19[0]).clear()
        self.Operation(*Common.element19, num)

    def img(self, file1, file2, file3, x=None):
        time.sleep(2)
        self.Operation(*Common.element20, file1)
        time.sleep(2)
        self.Operation(*Common.element21, file2)
        for i in file3:
            time.sleep(1)
            self.find_element(Common.element22[0]).clear()
            time.sleep(2)
            self.Operation(*Common.element22, i)
        if x != None:
            for i in range(x):
                time.sleep(1)
                self.Operation(*Common.element23)
                self.Operation(*Common.element24)

    def cd_worker(self, number):
        try:
            self.Operation(*Common.element27)

        except:
            pass
        '''输入手机号进行校验'''
        time.sleep(1)
        self.Operation(*Common.element25, number)
        self.Operation(*Common.element26)

    def up_worker(self, file_path):
        '''上传身份证头像'''
        self.Operation(*Common.element28, file_path)

    def clickup(self):
        '''点击提交'''
        self.Operation(*Common.element29)

    def shengfz(self, file_path1=None, file_path2=None, type_cl='身份证'):
        time.sleep(1)
        try:
            self.for_find_OP(Common.element30, type='click')
        except:
            pass

        '''选择证件类型自动上传图片'''
        self.for_find_OP(Common.element31, type_cl, 'click')
        try:
            self.find_element(Common.element32[0]).clear()
        except:
            pass

        if file_path1 is not None:
            if type_cl == '身份证':
                self.Operation(*Common.element33, file_path1)
                self.Operation(*Common.element34, file_path2)
            else:
                self.Operation(*Common.element32, file_path1)
        return type_cl



    def selects_Political(self, type):
        self.Operation(*Common.element35)
        self.for_find_OP(Common.element36, type, 'click')


    def job(self, text):
        self.Operation(*Common.element37, text)


    def setup_idcard(self, text, name):
        self.find_element(Common.element38[0]).clear()
        self.Operation(*Common.element38, text)
        self.find_element(Common.element39[0]).clear()
        self.Operation(*Common.element39, name)

    def select_Birthday(self, type_cl=None, year=None, mount=None, day=None):
        time.sleep(3)
        self.for_find_OP(Common.element31, type_cl, 'click')
        time.sleep(3)
        self.Operation(*Common.element40)
        time.sleep(1)
        years = int(self.find_element(Common.element41).text[0:-2])
        mounts = int(self.find_element(Common.element42).text[0:-2])
        if int(year) is not None:
            if int(year) < years:
                for i in range(years - int(year)):
                    self.Operation(*Common.element43)
            elif int(year) > years:
                for i in range(int(year) - years):
                    self.Operation(*Common.element44)
            else:
                pass
        if int(mount) is not None:
            if int(mount) < mounts:
                for i in range(mounts - int(mount)):
                    self.Operation(*Common.element45)
            elif int(mount) > mounts:
                for i in range(int(mount) - mounts):
                    self.Operation(*Common.element46)
            else:
                pass
        self.for_find_OP(Common.element47, day, 'click')
        return years



    def Relationship_type(self, type, text, parent_Community, Community, Floor, unit, Fl, roomId, file_path=None,
                          bt='确定'):
        time.sleep(3)
        """选择居住类型和居住关系"""

        self.for_find_OP(Common.element48, type, 'click')
        self.for_find_OP(Common.element49, text, 'click')

        if text == '租客':
            """当选择类型是租客的时候"""
            time.sleep(2)
            for c in file_path:
                if c:
                    """上传照片"""
                    self.Operation(*Common.element50, c)
                    self.find_element(Common.element50[0]).clear()
                else:
                    pass
        s = Mysqldb_test(parent_Community, Community, Floor, unit, Fl, roomId).mysqldn_01()
        # s=[0,123,1]
        time.sleep(10)
        self.clickup()

        if text == '租客':
            """如果是租客，并且该房间超员，上传照片也大于等与两张，我就点击确定/取消"""
            if len(file_path) >= 2 and (s[2] != 0 or s[0] == 0):

                t = self.find_elements(Common.element55)
                time.sleep(1)

                for i in t:
                    if i.text == bt:
                        i.click()
                        if bt == "确定":
                            self.c = Mysqldb_test.mysqldn_02(parent_Community, Community, Floor, unit, Fl, roomId)
            else:
                pass

    def devics(self, device, type):
        for i in device:
            if i:
                self.c.append(i)
        for i in type:
            if i:
                self.c.append(i)
        el = self.find_elements(Common.element56)
        list = [i.text for i in el]
        for i in self.c:
            if i not in list:
                return False
        return True



    def Issue_permissions(self, type, devse, num1=None, num2=None):
        s = self.find_elements(Common.element51)
        for i in type:
            for t in s:
                if i == t.text:
                    time.sleep(1)
                    t.click()
                    if i in '身份证绑定':
                        time.sleep(2)
                        self.Operation(*Common.element52, num1)
                    elif i in 'IC卡绑定':
                        time.sleep(2)
                        self.Operation(*Common.element53, num2)
                    break
        for c in devse:
            if c:
                self.for_find_OP(Common.element54, c, 'click')

    def up_issue(self):
        '''点击提交授权'''
        self.Operation(*Common.element57)



    def Verify_permissions(self, text=None, type='手机号'):
        '''搜索工作人员'''
        time.sleep(4)
        s3 = self.find_elements(Common.element63)
        for i in s3:
            if i.text == '居民列表':
                i.click()
        self.Operation(*Common.element58)
        self.for_find_OP(Common.element59, type, 'click')
        self.Operation(*Common.element60, text)
        self.Operation(*Common.element61)
        self.Operation(*Common.element62)
        time.sleep(1)
        self.for_find_OP((By.CSS_SELECTOR,'button.inlineBlock> span:nth-child(1)'),p='门禁授权',type='click')
        el = self.find_elements(Common.element56)
        list = [i.text for i in el]
        for i in self.c:
            if i not in list:
                return False
        return True
