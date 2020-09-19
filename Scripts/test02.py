import os
import re, time, datetime

from selenium.webdriver.common.by import By

from MYSQL.Mysql_Backup import Mysqldbbackup
import allure
import pytest
from Base.Make_date.idCard import IdNumber
from Common.common import Page
from Data import data_test02
from Scripts import test02

Scripts = test02()
curr_time = datetime.datetime.now()


# 完成后打开注释
d = None
driver = None

@pytest.fixture(scope='function', params=data_test02.list)
def param(request):
    return request.param


@pytest.fixture(scope='class', autouse=True)
def fix(conf_initdriver):
    global d
    global driver
    if not d and not driver:
        driver = conf_initdriver
        d = Page(driver).Resident()


class Test_2:


    def setup_class(self):
        self.d = d
        self.driver = driver

    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='登录测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('name,password', data_test02.login)
    def test_login(self, name, password):
        """
         登录测试
        描述：模拟了正确用户名错误用户名，
        正确/错误密码之间的组合加入校验
        """
        self.d.login(name, password)
        try:
            s = self.d.find_element(Scripts.element1, time=2).text

        except:
            s = self.driver.page_source

        if name == data_test02.login[0][0]:
            with allure.step('输入错误的账号登录'):
                allure.attach('参数', "账号：{0}  ；密码：{1}".format(name, password))

            with allure.step('断言:{0}'.format(s)):

                assert s in '该用户不存在!'



        # -------------------------------------------------------------------------------------------------------------------------------------
        elif name == data_test02.login[1][0]:
            with allure.step('输入错误的密码登录'):
                allure.attach('参数', "账号：{0}  ；密码：{1}".format(name, password))

            with  allure.step('断言：{0}'.format(s)):
                assert s == '用户名密码不正确!'

        elif name == data_test02.login[2][0]:
            with allure.step('输入正确的账号密码登录'):
                allure.attach('参数', "账号：{0}  ；密码：{1}".format(name, password))
                p = re.findall(Scripts.find, s)
            with  allure.step('断言：{0}'.format(p)):
                assert '数据看板首页' in p



    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='进入居民登记前的社区选择测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    @pytest.mark.parametrize('parent_Community,Community,Floor,unit,Fl,room', data_test02.select)
    def test_init(self, parent_Community, Community, Floor, unit, Fl, room):
        """
        选择登记房间
        选择不同的社区
        不同的社区不同的楼栋房间
        :param parent_Community:
        :param Community:
        :param Floor:
        :param unit:
        :param Fl:
        :param room:
        :return:
        """
        self.d.int(parent_Community, Community, Floor, unit, Fl, room)
        f = self.d.find_element(Scripts.element2).text
        with allure.step('输入错误的手机号'):
            allure.attach('参数',
                          "地址：社区：{0},小区：{1},楼栋：{2},单元：{3},楼层：{4},房间号：{5}".format(parent_Community, Community, Floor,
                                                                                 unit, Fl, room))

        assert Floor in f and unit in f and Fl in f and room in f



    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='产权人信息填写')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('file1,file2,file3,x', data_test02.file_path)
    @pytest.mark.parametrize('name, idcard, number, num', data_test02.owner_message)
    def test_01(self, name, idcard, number, num, file1, file2, file3, x):
        """图片校验:
        对图片能否上传成功做断言"""

        self.d.owner(name, idcard, number, num)

        self.d.img(file1, file2, file3, x)

        els = self.d.find_elements(Scripts.element21)

        assert len(els) == 2 + len(file3) - x


    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='手机号核验测试')
    @pytest.allure.severity('CRITTCAL')
    def test_02(self, param):
        """
              校验手机号:
              参数中加入了正确和错误的手机号，对不同情况做了断言
              """

        self.d.cd_worker(number=param)
        try:
            self.d.find_element(Scripts.element3).clear()
        except:
            pass

        if param == data_test02.list[0]:
            f = self.d.find_element(Scripts.element4).text
            assert f in '请输入正确的手机号'

        elif param == data_test02.list[1]:
            f = self.d.find_element(Scripts.element5).text
            assert f in '户口簿'

    @allure.step(title='对提交为空的测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_002(self):
        """
              '空提交',
              '校验不能为空提交！！！
              """
        time.sleep(1)
        self.d.clickup()
        el = self.d.find_element(Scripts.element6)
        s = el.text
        assert s in '请选择证件类型'


    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='身份证图片校验测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    @pytest.mark.parametrize('file_Path1,file_Path2,type_c', data_test02.file_path2)
    def test_003(self, file_Path1, file_Path2, type_c):
        """
               '身份证图片校验',
               '确保身份证合法有效
               :param file_Path1:
               :param file_Path2:
               :param type_c:
               :return:
               """

        type = self.d.shengfz(file_path1=file_Path1, file_path2=file_Path2, type_cl=type_c)

        if file_Path1 is not None:

            if '身份证正面照片' not in file_Path1 and '身份证反面照片' in file_Path2 and type == '身份证':
                s = self.d.find_element(Scripts.element7).text
                time.sleep(1)
                el = self.d.find_element(Scripts.element8).get_attribute('disabled')

                assert s in '请上传正确、清晰的身份证正面照片' and el == 'true'

            elif '身份证正面照片' in file_Path1 and '身份证反面照片' not in file_Path2 and type == '身份证':
                s = self.d.find_element(Scripts.element7).text
                time.sleep(1)
                el = self.d.find_element(Scripts.element9).get_attribute('disabled')

                assert s in '请上传正确、清晰的身份证反面照片' and el == 'true'


            elif '身份证正面照片' not in file_Path1 and '身份证反面照片' not in file_Path2 and type == '身份证':
                s = self.d.find_element(Scripts.element7).text
                time.sleep(1)
                el = self.d.find_element(Scripts.element10).get_attribute('disabled')

                assert s in '请上传正确、清晰的身份证反面照片' or '请上传正确、清晰的身份证正面照片' and el == None


            elif '身份证正面照片' in file_Path1 and '身份证反面照片' in file_Path2 and type == '身份证':
                time.sleep(2)
                el1 = self.d.find_element(Scripts.element8).get_attribute('disabled')
                el2 = self.d.find_element(Scripts.element9).get_attribute('disabled')
                time.sleep(1)

                assert el1 == 'true' and el2 == 'true'

            else:
                s = self.d.find_element(Scripts.element11).get_attribute('src')
                assert 'https://taijiashequ.oss-cn-beijing.aliyunc' in s


    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='上传头像验证')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('file_path', data_test02.file_path1)
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_004(self, file_path):
        """
             上传头像:
             判断了头像是否上传成功了

             :param file_path:
             :return:
             """
        self.d.up_worker(file_path)

        time.sleep(3)

        els = self.d.find_elements(Scripts.element12)

        x = 0
        z = 1
        if file_path == data_test02.file_path1[3]:
            for el in els:
                s = el.get_attribute('src')
                if file_path[-9:] in s:
                    z -= 1

        for el in els:
            s = el.get_attribute('src')
            if file_path[-9:] in s:
                x += 1
                break

        if x == 1 or z == 1:
            assert True

        else:
            assert False


    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='身份证输入校验')
    @pytest.mark.parametrize('idcard,name', data_test02.user)
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_005(self, idcard, name):
        """
                    身份证号码校验:
                     确保身份证号码合法有效
                    :param idcard:
                    :param name:
                    :return:
                    """
        self.d.setup_idcard(text=idcard, name=name)
        time.sleep(1)

        if data_test02.file_path == '身份证':

            if len(idcard) != 18:
                el = self.d.find_element(Scripts.element13).text

                assert el in '请输入正确的身份证号'

            elif len(idcard) == 18:
                idnumber = IdNumber(idcard)

                if idnumber.get_check_digit() == idcard[-1]:
                    assert True

                else:
                    el = self.d.find_element(Scripts.element13).text
                    assert el in '请输入正确的身份证号'



    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='年龄输入校验')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(data_test02.file_path2[-1][-1] == '身份证' or 1 == 2, reason='跳过')
    @pytest.mark.parametrize('day,year,mount', data_test02.Brithday)
    def test_006(self, day, year, mount):
        """
              工作人员年龄是否选中
              :param day:
              :param year:
              :param mount:
              :return
              """
        time.sleep(2)
        self.d.select_Birthday(type_cl=data_test02.file_path2[-1][-1], day=day, year=year, mount=mount)
        self.d.Operation(*Scripts.element14)
        s = self.d.find_elements(Scripts.element20)

        if s:
            assert True
        else:
            assert False




    # -------------------------------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize('type, text', data_test02.worker_job)
    def test_007(self, type, text):
        self.d.selects_Political(type)
        self.d.job(text)



    # -------------------------------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize('file_path', data_test02.file_list4)
    @pytest.mark.parametrize('type, text, bt', data_test02.Relationship_type)
    @pytest.mark.parametrize('parent_Community, Community, Floor, unit,Fl, roomId', [data_test02.select[-1]])
    def test_008(self, type, text, file_path, bt, parent_Community, Community, Floor, unit, Fl, roomId):
        """
                    上传一或两张租客照片，判断能否提交成功
                    :param type1:
                    :param type2:
                    :param type3:
                    :return:
                """
        try:
            els = self.d.find_elements(Scripts.element15)
            for i in els:
                time.sleep(1)
                self.d.Operation(*Scripts.element16)
                time.sleep(2)
                self.d.Operation(*Scripts.element17)
        except:
            pass
        time.sleep(2)

        self.d.Relationship_type(type=type, text=text, file_path=file_path, bt=bt, parent_Community=parent_Community,
                                 Community=Community, Floor=Floor, unit=unit, Fl=Fl, roomId=roomId)
        if len(file_path) < 2:
            try:
                el = self.d.find_element(Scripts.element18).text
            except:
                el = None
                print('这个用例在这里出错了。。。。。但是没关系继续走吧。。。。。')
                time.sleep(2)
                t = self.d.find_elements(Scripts.element24)
                time.sleep(1)
                for i in t:
                    if i.text == "取消":
                        i.click()
            assert el == '请上传两张或两张以上的租借合同'
        else:
            if bt == '确定':
                try:
                    dict1 = {}
                    time.sleep(30)
                    el = self.d.find_element(Scripts.element22).text
                    els = self.d.find_elements(Scripts.element23)

                    for i in els:
                        tex = i.text
                        list = tex.split('：')
                        dict1[list[0]] = list[-1]
                    dict1['姓名']=el
                    print(dict1)
                    assert data_test02.user[-1][0] in dict1['证件号码'] and data_test02.file_path2[-1][-1] in dict1['证件类型'] and \
                               data_test02.worker_job[-1][0] in dict1['政治面貌'] and data_test02.worker_job[-1][1] in dict1['职业'] and \
                           text in dict1['登记角色'] and data_test02.user[-1][-1] in dict1['姓名']
                except:
                      print("出现故障，无法跳转")
                      assert False

                finally:
                    Mysqldbbackup().backup_uesr()




    # -------------------------------------------------------------------------------------------------------------------------------------
    @allure.step(title='权限下发选择校验')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('type,devse,num1,num2', data_test02.Issue_permissions)
    @pytest.mark.skipif(1 == 2, reason='因为 test007 在执行时的bug导致后续程序无法进行')
    def test_009(self, type, devse, num1, num2):
        """
        点击权限:
        核验是否选择
        :param type:
        :param devse:
        :param num1:
        :param num2:
        :return:
        """
        self.d.Issue_permissions(type=type, devse=devse, num1=num1, num2=num2)
        device=self.d.devics(device=devse,type=type)
        if device:
             assert True
        else:
            assert False

    @allure.step(title='权限下发选择校验')
    @pytest.allure.severity('CRITTCAL')
    def test_010(self):
        self.d.up_issue()
        time.sleep(2)
        text=self.d.find_element((By.CSS_SELECTOR,'.el-message__content')).text
        assert "授权成功" in text



    @allure.step(title='权限下发选择校验')
    @pytest.allure.severity('CRITTCAL')
    def test_011(self):
        a=self.d.Verify_permissions(text=data_test02.list[-1])
        if a:
            assert True
        else:
            assert Falsedata_test01





  # -------------------------------------------------------------------------------------------------------------------------------------
    def teardown_class(self):
        path = os .path.join(os.getcwd(), "Report\结果图")
        filename = os.path.join(path, 'test01.png')
        self.d.page('get_screenshot_as_file', filepath=filename)
        # self.d.page('get_screenshot_as_file', filepath='./test01结果图.png')
        del self.d
        del self.driver


if __name__ == '__main__':
    pytest.main('-s -html=../Report/report.html test02.py')
