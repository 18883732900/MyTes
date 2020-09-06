import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base.base import Base
from Base.initdriver import inidriver
from Common import upload_worker
Common=upload_worker()


class uploda(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    def login(self,name=None,password=None):
        self.find_element(Common.user_name[0]).clear()
        self.find_element(Common.user_password[0]).clear()
        self.Operation(*Common.user_name, name)
        self.Operation(*Common.user_password, password)
        self.Operation(*Common.login)
        time.sleep(3)

    def int(self,parent_Community, Community, Floor, unit):
        '''
              element1: 定位人房信息
              element2：定位工作人员信息管理
              element3：定位工作人员登记
              element4: 定位点击社区输入框
              element5：定位社区选项
              element6：定位点击小区输入框
              element7: 定位选择小区
              element8：定位楼栋输入框
              element9：定位选择楼栋
              element10：定位单元输入框
              element11：定位单元选项
              element12：定位b办理按钮
              如需修改参数在
              :return:
              '''
        s1=self.find_elements(Common.element1)
        for i in s1:
            if i.text=='人房信息':
                i.click()
        s2=self.find_elements(Common.element2)
        for i in s2:
            if i.text == '工作人员管理':
                i.click()
        s3=self.find_elements(Common.element3)
        for i in s3:
            if i.text == '工作人员登记':
                i.click()
        time.sleep(2)
        self.Operation(*Common.element4)
        s1 = self.find_elements(Common.element5)
        for i in s1:
            if parent_Community in i.text:
                i.click()
                break
        self.Operation(*Common.element6)
        s2 = self.find_elements(Common.element7)
        for i in s2:
            if Community in i.text:
                i.click()
                break
        self.Operation(*Common.element8)
        s3 = self.find_elements(Common.element9)
        for i in s3:
            if Floor in i.text:
                i.click()
                break
        self.Operation(*Common.element10)
        s4 = self.find_elements(Common.element11)
        for i in s4:
            if unit in i.text:
                i.click()
                break
        self.Operation(*Common.element12)

    def cd_worker(self, number):
        '''输入手机号进行校验'''
        # time.sleep(1)
        self.Operation(*Common.element13, number)
        # time.sleep(1)
        self.Operation(*Common.element14)

    def up_worker(self, file_path):
        '''上传身份证头像'''
        # time.sleep(2)
        self.Operation(*Common.element15, file_path)

    def clickup(self):
        '''点击提交'''
        self.Operation(*Common.element16)


    def shengfz(self, file_path1=None, file_path2=None, type_cl='身份证'):
        time.sleep(1)
        try:
            els = self.find_elements(Common.element38)
            for i in els:
                i.click()
        except:
            pass

        '''选择证件类型自动上传图片'''
        els = self.find_elements(Common.element18)
        for i in els:
            if i.text == type_cl:
                i.click()
                break
        try:
            self.find_element(Common.element20[0]).clear()
        except:
            pass

        if file_path1 is not None:
            if type_cl == '身份证':
                self.Operation(*Common.element17, file_path1)
                self.Operation(*Common.element19, file_path2)
            else:
                self.Operation(*Common.element20, file_path1)
        return type_cl
    def selects_Political(self,type):
        self.Operation(*Common.element29)
        els=self.find_elements(Common.element30)
        for i in els:
            if i.text==type:
                i.click()
                break
    def job(self,text):
        self.Operation(*Common.element31,text)
    def setup_idcard(self,text,name):
        self.find_element(Common.element32[0]).clear()
        self.Operation(*Common.element32,text)
        self.find_element(Common.element33[0]).clear()
        self.Operation(*Common.element33,name)

    def select_Birthday(self,type_cl=None,year=None, mount=None, day=None):
        time.sleep(3)
        els = self.find_elements(Common.element18)
        for i in els:
            if i.text==type_cl:
                i.click()
                break
        time.sleep(3)
        self.Operation(*Common.element21)
        years =int(self.find_element(Common.element22).text[0:-2])
        # print(years)
        mounts = int(self.find_element(Common.element23).text[0:-2])
        if int(year) is not None:
            if int(year) < years:
                for i in range(years - int(year)):
                    self.Operation(*Common.element25)
            elif int(year) > years:
                for i in range(int(year) - years):
                    self.Operation(*Common.element26)
            else:
                pass
        if  int(mount) is not None:
            if int(mount) < mounts:
                for i in range(mounts - int(mount)):
                    self.Operation(*Common.element27)
            elif int(mount) > mounts:
                for i in range(int(mount) - mounts):
                    self.Operation(*Common.element28)
            else:
                pass
        elp = self.find_elements(Common.element24)
        for i in elp:
            if i.text == day:
                # print(i.text)
                i.click()
                break
        return years
    def work_type(self,text):

        els=self.find_elements(Common.element34)
        for i in els:
            if i.text==text:
                i.click()
                break

    def Issue_permissions(self,type,devse,num1=None,num2=None):
        s=self.find_elements(Common.element35)

        for i in type:
            for t in s:
               if i==t.text:
                   t.click()
                   if i in '身份证绑定':
                       self.Operation(*Common.element36,num1)
                   elif i in 'IC卡绑定':
                       self.Operation(*Common.element37, num2)
                   break
        p=self.find_elements(Common.element40)
        for c in devse:
            for e in p:
                if c in e.text:
                    # print(e.text)
                    time.sleep(5)
                    e.click()
                    break

    def up_issue(self):
        self.Operation(*Common.element39)

    def Verify_permissions(self,text=None,type='手机号'):
        self.Operation(*Common.element41)
        s=self.find_elements(Common.element42)
        for i in s :
            if i.text==type:
                i.click()
        self.Operation(*Common.element43,text)
        self.Operation(*Common.element44)
        self.Operation(*Common.element45)




