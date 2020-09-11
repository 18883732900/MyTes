import re, pytest, time, datetime
import allure
from Scripts import test01
from selenium.webdriver.common.by import By
from Base.initdriver import inidriver
from Base.number import number
from Base.Backup import Mysqldbbackup
from Common.common import Page
from Data import data_test01
from Base.idCard import IdNumber

curr_time = datetime.datetime.now()
Scripts = test01()


@pytest.fixture(scope='function', params=data_test01.list)
def param(request):
    return request.param


@pytest.fixture(scope='class', autouse=True)
def fix(conf_initdriver):
    global d
    global driver
    driver = conf_initdriver
    d = Page(driver).uploda()


class Test_1:

    def setup_class(self):
        self.d = d
        self.driver = driver

    """
      方法：@pytest.allure.severity(Severity)
    参数：
        Severity：严重级别(BLOCKER,CRITICAL,NORMAL,MINOR,TRIVIAL)
    使用方式：
        @pytest.allure.severity(pytest.allure.severity_level.CRITICAL）
        
        """

    @allure.step(title='登录测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('name,password', data_test01.login)
    def test_login(self, name, password):

        """
               登录测试
              描述：模拟了正确用户名错误用户名，
              正确/错误密码之间的组合加入校验
              """

        self.d.login(name, password)
        try:
            s = self.d.find_element(Scripts.element1, time=3).text

        except:
            s = self.driver.page_source

        if name == data_test01.login[0][0]:
            with allure.step('输入错误的账号登录'):
                allure.attach('参数', "账号：{0}  ；密码：{1}".format(name, password))

            with allure.step('断言:{0}'.format(s)):
                assert s in '该用户不存在!'

        elif name == data_test01.login[1][0]:
            with allure.step('输入错误的密码登录'):
                allure.attach('参数', "账号：{0}  ；密码：{1}".format(name, password))

            with  allure.step('断言：{0}'.format(s)):

                assert s in '用户名密码不正确!'

        elif name == data_test01.login[2][0]:
            with allure.step('输入正确的账号密码登录'):
                allure.attach('参数', "账号：{0}  ；密码：{1}".format(name, password))
                p = re.findall(Scripts.find, s)

            with  allure.step('断言：{0}'.format(p)):
                assert '数据看板首页' in p

    @allure.step(title='进入工作人员登记前的社区选择测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    @pytest.mark.parametrize('parent_Community,Community,Floor,unit', data_test01.select)
    def test_init(self, parent_Community, Community, Floor, unit):
        """
        选择不同的社区:
        不同的社区不同的楼栋关联不同的物业
        """
        self.d.int(parent_Community, Community, Floor, unit)
        f = self.d.find_element(Scripts.element6).text
        with allure.step('输入错误的手机号'):
            allure.attach('参数', "地址：社区：{0},小区：{1},楼栋：{2},单元：{3}".format(parent_Community,Community,Floor,unit))
        assert f in '工作人员类别列表'

    def teardown_class(self):

        # self.d.page('get_screenshot_as_file', filepath='./结果图.png')
        del self.d
        del self.driver

    @allure.step(title='手机号核验测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_001(self, param):
        """
        校验手机号:
        参数中加入了正确和错误的手机号，对不同情况做了断言
        """
        s = param
        self.d.cd_worker(number=s)
        try:
            self.d.find_element(Scripts.element5).clear()

        except:
            pass

        if s == data_test01.list[0]:

            f = self.d.find_element(Scripts.element3).text
            with allure.step('输入错误的手机号'):
                allure.attach('参数', "手机号：{0}".format(s))
            with  allure.step('断言：{0} in 请输入正确的手机号'.format(f)):
                assert f in '请输入正确的手机号'

        elif s == data_test01.list[1]:

            f = self.d.find_element(Scripts.element4).text
            with allure.step('输入正确的手机号'):
                allure.attach('参数', "手机号：{0}".format(s))
            with  allure.step('断言：{0}in 户口簿'.format(f)):
                assert f in '户口簿'

    @allure.step(title='对提交为空的测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_002(self):
        """
        '空提交',
        '校验不能为空提交！！！
        """

        self.d.clickup()

        el = self.d.find_element(Scripts.element7)

        s = el.text
        with  allure.step('断言：{0} in  请选择证件类型'.format(s)):
           assert s in '请选择证件类型'

    @allure.step(title='身份证图片校验测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    @pytest.mark.parametrize('file_Path1,file_Path2,type_c', data_test01.file_path)
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
                s = self.d.find_element(Scripts.element9).text
                time.sleep(1)
                el = self.d.find_element(Scripts.element16).get_attribute('disabled')
                with allure.step('输入错的身份证正面照片'):
                    allure.attach('参数', "照片：{0}{1},类型：{2}".format(file_Path1,file_Path2,type_c))
                assert s in '请上传正确、清晰的身份证正面照片' and el == 'true'

            elif '身份证正面照片' in file_Path1 and '身份证反面照片' not in file_Path2 and type == '身份证':
                s = self.d.find_element(Scripts.element9).text
                time.sleep(1)
                el = self.d.find_element(Scripts.element17).get_attribute('disabled')

                assert s in '请上传正确、清晰的身份证反面照片' and el == 'true'


            elif '身份证正面照片' not in file_Path1 and '身份证反面照片' not in file_Path2 and type == '身份证':
                s = self.d.find_element(Scripts.element9).text
                time.sleep(1)
                el = self.d.find_element(Scripts.element18).get_attribute('disabled')
                with allure.step('输入错的身份证反面照片'):
                    allure.attach('参数', "照片：{0}{1},类型：{2}".format(file_Path1,file_Path2,type_c))

                assert s in '请上传正确、清晰的身份证反面照片' or '请上传正确、清晰的身份证正面照片' and el == None

            elif '身份证正面照片' in file_Path1 and '身份证反面照片' in file_Path2 and type == '身份证':
                time.sleep(4)
                el1 = self.d.find_element(Scripts.element16).get_attribute('disabled')
                el2 = self.d.find_element(Scripts.element17).get_attribute('disabled')
                time.sleep(1)
                with allure.step('输入正确的身份证照片'):
                    allure.attach('参数', "照片：{0}{1},类型：{2}".format(file_Path1,file_Path2,type_c))

                assert el1 == 'true' and el2 == 'true'

            else:
                s = self.d.find_element(Scripts.element12).get_attribute('src')
                with allure.step('输入其他证件照片'):
                    allure.attach('参数', "照片：{0}{1},类型：{2}".format(file_Path1,file_Path2,type_c))

                assert 'https://taijiashequ.oss-cn-beijing.aliyunc' in s



    @allure.step(title='上传头像验证')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('file_path', data_test01.file_path1)
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

        els = self.d.find_elements(Scripts.element8)

        x = 0
        z = 0
        for el in els:
            s = el.get_attribute('src')
            if data_test01.file[-9:] in s:
                x += 1
                return x

        if file_path == data_test01.file_path1[3]:
            for el in els:
                s = el.get_attribute('src')
                if file_path[-9:] in s:
                    z -= 1

        if x == 1 or z == 1:
            assert True
        else:
            assert False



    @allure.step(title='身份证号码输入验证')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('idcard,name', data_test01.user)
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
        if data_test01.file_path == '身份证':
            if len(idcard) != 18:
                el = self.d.find_element(Scripts.element15).text
                assert el in '请输入正确的身份证号'
            elif len(idcard) == 18:
                idnumber = IdNumber(idcard)
                if idnumber.get_check_digit() == idcard[-1]:
                    assert True
                else:
                    el = self.d.find_element(Scripts.element15).text
                    assert el in '请输入正确的身份证号'

    @allure.step(title='工作人员年龄输入校验')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(data_test01.file_path[-1][-1] == '身份证' or 1 == 2, reason='跳过')
    @pytest.mark.parametrize('day,year,mount', data_test01.Brithday)
    def test_006(self, day, year, mount):
        """
        工作人员年龄校验', '确保工作人员合法参加工作
        :param day:
        :param year:
        :param mount:
        :return:
        """
        time.sleep(2)
        self.d.select_Birthday(type_cl=data_test01.file_path[-1][-1], day=day, year=year, mount=mount)
        self.d.clickup()
        if curr_time.year - int(year) < 16:
            a = self.d.find_element(Scripts.element14).text
            assert a in '工作人员年龄不能小于16岁'
        else:
            assert True

    @allure.step(title='提交后反显校验')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('type1,type2,type3', data_test01.worker_job)
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_007(self, type1, type2, type3):
        """
        返显校验:
        确保上传信息都有效
        :param type1:
        :param type2:
        :param type3:
        :return:
        """
        time.sleep(3)
        self.d.selects_Political(type=type1)
        self.d.job(text=type2)
        self.d.work_type(text=type3)
        time.sleep(3)
        self.d.clickup()
        dict1 = {}
        time.sleep(12)
        els = self.d.find_elements(Scripts.element19)
        for i in els:
            text = i.text
            list = text.split('：')
            dict1[list[0]] = list[-1]
        el = self.d.find_element(Scripts.element20).text
        time.sleep(1)
        assert data_test01.user[-1][0] in dict1['证件号码'] and data_test01.file_path[-1][-1] in dict1['证件类型'] and type1 in \
               dict1['政治面貌'] \
               and type2 in dict1['职业'] and type3 in dict1['登记角色'] and data_test01.user[-1][-1] in el

    @allure.step(title='权限下发选择校验')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('type,devse,num1,num2', data_test01.Issue_permissions)
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_008(self, type, devse, num1, num2):
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
        els = self.d.find_elements(Scripts.element21)
        list = [i.text for i in els]
        x = 0
        for i in type:
            if i in list:
                x += 1
        y = 0
        for i in devse:
            if i in list:
                y += 1
        assert x + y == len(type) + len(devse)

    @allure.step(title='检查提交按钮是否自动进行页面跳转')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_009(self):
        """
        点击授权检测页面跳转:
        确保成功点击授权
        :return:
        """
        self.d.up_issue()
        time.sleep(3)
        try:
            s3 = self.d.find_elements(Scripts.element22)
            for i in s3:
                if i.text == '工作人员列表':
                    i.click()
                    Mysqldbbackup().backup_worker()
                    assert True
        except:
            assert False

    @allure.step(title='在工作人员列表中核对基本数据')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_010(self):
        """
        核对', '确保上传信息都正确'
        :return:
        """
        time.sleep(3)
        s = self.d.page(fun='driver.page_source')
        x = 0
        list = [i for i in data_test01.select[-1]]

        list.insert(0, data_test01.user[-1][-1])
        for i in list:
            if i in s:
                x += 1

        assert x == len(list)

    @allure.step(title='在工作人员列表中门禁里检测上次填入信息是否成功带入')
    @pytest.allure.severity('CRITTCAL')
    def test_011(self):
        """
        返显校验:
         权限带入正常
        :return:
        """
        self.d.Verify_permissions(text=data_test01.list[-1])
        els = self.d.find_elements(Scripts.element21)
        list = [i.text for i in els]
        self.d.implicitly_wait(30)
        x = 0
        y = 0
        z = 0
        type = data_test01.Issue_permissions[-1][0]
        for i in type:
            if i in list:
                x += 1
        deves = data_test01.Issue_permissions[-1][1]
        for i in deves:
            if i in list:
                y += 1
        text = self.d.find_elements(Scripts.element24)
        for i in text:
            text1 = i.get_attribute('value')
            if text1 in data_test01.Issue_permissions[-1][2] or data_test01.Issue_permissions[-1][3]:
                z += 1
        assert x + y + z == len(type) + len(deves) + 2


if __name__ == '__main__':
    pytest.main('-s -html=./Report/report.html test01.py')
