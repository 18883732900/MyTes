import time
from selenium.webdriver.common.by import By
from Base.base import Base
from Common import Resident_check_in_data
from Base.Mysqldb_test import Mysqldb_test

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
        self.for_find_OP(Common.element1, '人房信息','click')
        self.for_find_OP(Common.element2,'居民信息管理','click')
        self.for_find_OP(Common.element3,'居民入住登记','click')
        time.sleep(2)
        self.Operation(*Common.element4)
        self.for_find_OP(Common.element5,parent_Community,'click')
        self.Operation(*Common.element6)
        self.for_find_OP(Common.element7,Community,'click')
        self.Operation(*Common.element8)
        self.for_find_OP(Common.element9,Floor,'click')
        self.Operation(*Common.element10)
        self.for_find_OP(Common.element11,unit,'click')
        self.Operation(*Common.element12)
        self.for_find_OP(Common.element13,FL,'click')
        self.for_find_OP(Common.element14,roomId, 'click')

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
        self.for_find_OP(Common.element31,type_cl,'click')
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
        elp = self.find_elements(Common.element47)
        for i in elp:
            if i.text == day:
                # print(i.text)
                i.click()
                break
        return years

    def Relationship_type(self, type, text,parent_Community, Community, Floor, unit, Fl , roomId, file_path=None, bt='确定'):
        time.sleep(4)

        self.for_find_OP(Common.element48,type, 'click')
        self.for_find_OP(Common.element49,text, 'click')
        if text == '租客':
            time.sleep(2)
            for c in file_path:
                if c :
                   self.Operation(*Common.element50, c)
                   self.find_element(Common.element50[0]).clear()
                else:
                    pass
        s = Mysqldb_test().mysqldn_01(parent_Community, Community, Floor, unit,Fl,roomId)
        time.sleep(10)
        self.clickup()
        if text == '租客' :
            if s[1] != 0 or s[0] == 0 and len(file_path) >= 2:
                t = self.find_elements(Common.element55[0])
                time.sleep(1)
                for i in t:
                    if i.text == bt:
                        i.click()
            else:
                pass

    def Issue_permissions(self, type, devse, num1=None, num2=None):
        s = self.find_elements(Common.element51)
        for i in type:
            for t in s:
                if i == t.text:
                    t.click()
                    if i in '身份证绑定':
                        self.Operation(*Common.element52, num1)
                    elif i in 'IC卡绑定':
                        self.Operation(*Common.element53, num2)
                    break
        p = self.find_elements(Common.element54)
        for c in devse:
            for e in p:
                if c in e.text:
                    # print(e.text)
                    time.sleep(5)
                    e.click()
                    break


if __name__ == '__main__':
    pass
    print(1 << 3)
