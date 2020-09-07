
import re,time,datetime
from Base.Backup import Mysqldbbackup
import allure
import pytest
from selenium.webdriver.common.by import By

from Base.idCard import IdNumber
from Base.initdriver import inidriver
from Common.common import Page
from Data import data_test02
from Scripts import test02

Scripts=test02()
curr_time = datetime.datetime.now()
@pytest.fixture(scope='function', params=data_test02.list)
def param(request):
    return request.param

class Test_2:
    def setup_class(self):
        self.driver = inidriver('http://test.bjhontai.com:180/#/login')
        self.driver.maximize_window()
        self.d = Page(self.driver).Resident()
    @allure.step(title='登录测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('name,password', data_test02.login)
    def test_login(self,name,password):
        self.d.login(name, password)
        allure.attach('登录测试', '模拟了正确用户名错误用户名，正确/错误密码之间的组合加入校验')
        if name == data_test02.login[0][0]:
            s = self.d.find_element(Scripts.element1).text
            assert s in '该用户不存在!'
        elif name == data_test02.login[1][0]:
            s = self.d.find_element(Scripts.element1).text
            assert s in '用户名密码不正确!'
        elif name == data_test02.login[2][0]:
            s = self.driver.page_source
            p = re.findall(
                r'<div id="tab-/index" aria-controls="pane-/index" role="tab" aria-selected="true" tabindex="0" class="el-tabs__item is-top is-active">(.+?)</div>',
                s)
            assert '数据看板首页' in p

    @allure.step(title='进入居民登记前的社区选择测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    @pytest.mark.parametrize('parent_Community,Community,Floor,unit,Fl,room', data_test02.select)
    def test_init(self, parent_Community, Community, Floor, unit,Fl,room):
            allure.attach('选择不同的社区', '不同的社区不同的楼栋房间')
            self.d.int(parent_Community, Community, Floor, unit,Fl,room)
            f = self.d.find_element(Scripts.element2).text
            assert  Floor  in f and unit in f and Fl  in f and   room  in f

    def teardown_class(self):
        self.d.page('get_screenshot_as_file', filepath='./结果图.png')
        time.sleep(5)

    @allure.step(title='产权人信息填写')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('file1,file2,file3,x',data_test02.file_path)
    @pytest.mark.parametrize('name, idcard, number, num', data_test02.owner_message)
    def test_01(self,name, idcard, number, num,file1,file2,file3,x):
        allure.attach('图片校验', '对图片能否上传成功做断言')
        self.d.owner(name, idcard, number, num)
        self.d.img(file1,file2,file3,x)
        els=self.d.find_elements((By.CSS_SELECTOR,'[class="el-image__inner el-image__preview"]'))
        # print(len(els))
        assert len(els)==2+len(file3)-x

    @allure.step(title='手机号核验测试')
    @pytest.allure.severity('CRITTCAL')
    def test_02(self,param):
        allure.attach('校验手机号', '参数中加入了正确和错误的手机号，对不同情况做了断言')
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
            # print(f)
            assert f in '户口簿'

    @allure.step(title='对提交为空的测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_002(self):
        allure.attach('空提交', '校验不能为空提交！！！')
        time.sleep(1)
        self.d.clickup()
        el = self.d.find_element(Scripts.element6)
        s = el.text
        # print(s)
        assert s in '请选择证件类型'

    @allure.step(title='身份证图片校验测试')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(1 == 2, reason='跳过')
    @pytest.mark.parametrize('file_Path1,file_Path2,type_c', data_test02.file_path2)
    def test_003(self, file_Path1, file_Path2, type_c):
        allure.attach('身份证图片校验', '确保身份证合法有效')
        # print(file_Path1)
        type = self.d.shengfz(file_path1=file_Path1, file_path2=file_Path2, type_cl=type_c)
        # time.sleep(2)
        if file_Path1 is not None:
            if '身份证正面照片' not in file_Path1 and '身份证反面照片' in file_Path2 and type == '身份证':
                s = self.d.find_element(Scripts.element7).text
                # print(s)
                # time.sleep(2)
                time.sleep(1)
                el = self.d.find_element(Scripts.element8).get_attribute('disabled')
                # print(el)

                assert s in '请上传正确、清晰的身份证正面照片' and el == 'true'

            elif '身份证正面照片' in file_Path1 and '身份证反面照片' not in file_Path2 and type == '身份证':
                s = self.d.find_element(Scripts.element7).text
                # print(s)
                # time.sleep(2)
                time.sleep(1)
                el = self.d.find_element(Scripts.element9).get_attribute('disabled')
                assert s in '请上传正确、清晰的身份证反面照片' and el == 'true'


            elif '身份证正面照片' not in file_Path1 and '身份证反面照片' not in file_Path2 and type == '身份证':
                s = self.d.find_element(Scripts.element7).text
                # print(s)
                time.sleep(1)
                el = self.d.find_element(Scripts.element10).get_attribute('disabled')
                # print(el)
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

    @allure.step(title='上传头像验证')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.parametrize('file_path', data_test02.file_path1)
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_004(self, file_path):
            self.d.up_worker(file_path)
            time.sleep(3)
            els = self.d.find_elements(Scripts.element12)
            x = 0
            for el in els:
                s = el.get_attribute('src')
                if file_path[-9:] in s:
                    x += 1
                    return x
            if x == 1:
                assert True
            else:
                assert False
    @pytest.mark.parametrize('idcard,name', data_test02.user)
    @pytest.mark.skipif(1 == 2, reason='跳过')
    def test_005(self, idcard, name):
        self.d.setup_idcard(text=idcard, name=name)
        allure.attach('上传头像', '判断了头像是否上传成功了')
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

    @allure.step(title='年龄输入校验')
    @pytest.allure.severity('CRITTCAL')
    @pytest.mark.skipif(data_test02.file_path2[-1][-1] == '身份证' or 1 == 2, reason='跳过')
    @pytest.mark.parametrize('day,year,mount', data_test02.Brithday)
    def test_006(self, day, year, mount):
        time.sleep(2)
        self.d.select_Birthday(type_cl=data_test02.file_path2[-1][-1], day=day, year=year, mount=mount)
        self.d.Operation(*Scripts.element14)
        s=self.d.find_elements((By.CLASS_NAME,"el-input__icon.el-icon-circle-close"))
        if s:
            assert True
        else:
            assert False

    @pytest.mark.parametrize('type, text', data_test02.worker_job)
    def test_008(self,type,text):
        self.d.selects_Political(type)
        self.d.job(text)

    @pytest.mark.parametrize('file_path',data_test02.file_list4)
    @pytest.mark.parametrize('type, text, bt', data_test02.Relationship_type)
    def test_007(self,type, text, file_path, bt):
        self.d.Relationship_type(type, text, file_path, bt)
        if len(file_path)<2:
            pass
        else:
            if bt=='确定':
              Mysqldbbackup().backup_uesr()
              pass






if __name__ == '__main__':
    pytest.main('-s -html=../Report/report.html test02.py')
