from selenium.webdriver.common.by import By
from Base.idCard import IdNumber
from Base.number import number
from Base.name import name

user_name = ((By.CSS_SELECTOR, '[placeholder="请输入账号"]'), 'send_keys')
user_password = ((By.CSS_SELECTOR, '[placeholder="请输入密码"]'), 'send_keys')
login = ((By.XPATH, '/html/body/div/div[2]/div/form/div[4]/div/button/span'), 'click')

'''
name=姓名
idcard=身份证号
number=手机号
'''
name = name()
idcard = IdNumber.generate_myid()
number = number()


class upload_worker():
    user_name = ((By.CSS_SELECTOR, '[placeholder="请输入账号"]'), 'send_keys')
    user_password = ((By.CSS_SELECTOR, '[placeholder="请输入密码"]'), 'send_keys')
    login = ((By.XPATH, '/html/body/div/div[2]/div/form/div[4]/div/button/span'), 'click')
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
        element12：定位提交按钮
        如需修改参数在
        :return:
        '''
    element1 = (By.CSS_SELECTOR,
                '.el-menu-vertical-demo > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > div:nth-child(1) > span:nth-child(2)')
    element2 = (
        By.CSS_SELECTOR,
        '.is-opened > ul:nth-child(2) > div > div> li:nth-child(1) > div:nth-child(1) > span:nth-child(2)')
    element3 = (By.CSS_SELECTOR,
                '.el-menu-vertical-demo > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > div:nth-child(1) > div:nth-child(4) > li:nth-child(1) > ul:nth-child(2) > div:nth-child(1) > div > li:nth-child(1) > span:nth-child(2)')
    element4 = ((By.CSS_SELECTOR, '[placeholder="请选择社区"]'), 'click')
    element5 = (By.CSS_SELECTOR,
                'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li > span')
    element6 = ((By.CSS_SELECTOR, '[placeholder="请选择小区"]'), 'click')
    element7 = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li/span')
    element8 = ((By.CSS_SELECTOR, '[placeholder="请选择楼栋"]'), 'click')
    element9 = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li/span')
    element10 = ((By.CSS_SELECTOR, '[placeholder="请选择单元"]'), 'click')
    element11 = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li/span')
    element12 = (
        (By.XPATH, '/html/body/section/section/main/div/div[2]/div/div/div[1]/div/div/div/div/div[5]/div/span'),
        'click')
    '''定位手机号输入框'''
    element13 = ((By.CSS_SELECTOR, '[placeholder="请输入手机号"]'), 'send_keys')
    '''确认按钮'''
    element14 = ((By.XPATH, '/html/body/div[5]/div/div[2]/div/div/div[2]/button'), 'click')
    '''插入头像图片'''
    element15 = ((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[4]/div/div[1]/div/input'), 'send_keys')
    '''点击提交'''
    element16 = ((By.CSS_SELECTOR, 'button.btn:nth-child(2) > span:nth-child(1)'), 'click')
    '''定位证件类型'''
    element18 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/button/span')
    '''发送身份证正面照'''
    element17 = ((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/input'), 'send_keys')
    '''反面照'''
    element19 = ((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/input'), 'send_keys')
    '''发送普通证件图片'''
    element20 = ((By.CSS_SELECTOR,
                  'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(3) > div.uploadInfo.clearfix.ml-30 > div.upload.fl.mt-20 > input'),
                 'send_keys')
    element21 = ((By.CSS_SELECTOR, '[placeholder="请选择出生日期"]'), 'click')
    element22 = (By.CSS_SELECTOR, 'span.el-date-picker__header-label:nth-child(3)')
    element23 = (By.CSS_SELECTOR, 'span.el-date-picker__header-label:nth-child(4)')
    element24 = (By.CSS_SELECTOR, '[class="available"] > div >span')
    element25 = ((By.CSS_SELECTOR, '[aria-label="前一年"]'), 'click')
    element26 = ((By.CSS_SELECTOR, '[aria-label="后一年"]'), 'click')
    element27 = ((By.CSS_SELECTOR, '[aria-label="上个月"]'), 'click')
    element28 = ((By.CSS_SELECTOR, '[aria-label="下个月"]'), 'click')
    element29 = ((By.CSS_SELECTOR, '[placeholder="请选择政治面貌"]'), 'click')
    element30 = (By.XPATH, '/html/body/div[last()]/div[1]/div[1]/ul/li/span')
    element31 = ((By.CSS_SELECTOR, '[placeholder="请输入职业"]'), 'send_keys')
    element32 = ((By.CSS_SELECTOR, '[placeholder="请输入证件号码"]'), 'send_keys')
    element33 = ((By.CSS_SELECTOR, '[placeholder="请输入姓名"]'), 'send_keys')
    element34 = (By.CSS_SELECTOR, 'button.buttonStyle > span')
    element35 = (By.CSS_SELECTOR, 'div.item> label > span:nth-child(2) > span:nth-child(2)')
    element36 = ((By.CSS_SELECTOR, '[placeholder="身份证编号(必填)"]'), 'send_keys')
    element37 = ((By.CSS_SELECTOR, '[placeholder="Ic卡(必选)"]'), 'send_keys')
    element38 = (By.CSS_SELECTOR, ' .cardImgView > div> i:nth-child(1)')
    element39 = ((By.CSS_SELECTOR, 'span.historyBtn:nth-child(1)'), 'click')
    element40 = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[5]/div[2]/div/label/span[2]')
    element41 = ((By.CSS_SELECTOR, '[placeholder="姓名"]'), 'click')
    element42 = (By.XPATH, ' /html/body/div/div[1]/div[1]/ul/li/span')
    element43 = ((By.CSS_SELECTOR, '[placeholder="请输入内容"]'), 'send_keys')
    element44 = ((By.CSS_SELECTOR, 'span.searchBtn:nth-child(1)'), 'click')
    element45 = ((By.CSS_SELECTOR,
                  '.el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > div:nth-child(1) > button:nth-child(3)'),
                 'click')


class Resident_check_in():
    user_name = ((By.CSS_SELECTOR, '[placeholder="请输入账号"]'), 'send_keys')
    user_password = ((By.CSS_SELECTOR, '[placeholder="请输入密码"]'), 'send_keys')
    login = ((By.XPATH, '/html/body/div/div[2]/div/form/div[4]/div/button/span'), 'click')
    element1 = (By.CSS_SELECTOR,
                '.el-menu-vertical-demo > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > div:nth-child(1) > span:nth-child(2)')
    element2 = (
        By.CSS_SELECTOR,
        '.is-opened > ul:nth-child(2) > div > div> li:nth-child(1) > div:nth-child(1) > span:nth-child(2)')
    element3 = (By.CSS_SELECTOR,
                '.el-menu-vertical-demo > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > div:nth-child(1) > div > li:nth-child(1) > ul:nth-child(2) > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > span:nth-child(2)')
    element4 = ((By.CSS_SELECTOR, '[placeholder="请选择社区"]'), 'click')
    element5 = (By.CSS_SELECTOR,
                'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li > span')
    element6 = ((By.CSS_SELECTOR, '[placeholder="请选择小区"]'), 'click')
    element7 = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li/span')
    element8 = ((By.CSS_SELECTOR, '[placeholder="请选择楼栋"]'), 'click')
    element9 = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li/span')
    element10 = ((By.CSS_SELECTOR, '[placeholder="请选择单元"]'), 'click')
    element11 = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li/span')
    element12 = ((By.CSS_SELECTOR, '[placeholder="请选择楼层"]'), 'click')
    element13 = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li/span')
    element14 = (By.CSS_SELECTOR, 'div.doorNum > p:nth-child(2)')
    element15 = ((By.CSS_SELECTOR, '.saveBtn'), 'click')
    element16 = ((By.CSS_SELECTOR, '[placeholder="请输入产权人姓名"]'), 'send_keys')
    element17 = ((By.CSS_SELECTOR, '[placeholder="请输入产权人身份证号"]'), 'send_keys')
    element18 = ((By.CSS_SELECTOR, '[placeholder="请输入产权人手机号"]'), 'send_keys')
    element19 = ((By.CSS_SELECTOR, '[placeholder="请输入产权证号"]'), 'send_keys')
    element20 = (
        (By.CSS_SELECTOR, '.uploadInfo > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)'),
        'send_keys')
    element21 = ((By.CSS_SELECTOR, 'div.upload:nth-child(3) > input:nth-child(2)'), 'send_keys')
    element22 = (
        (By.CSS_SELECTOR, '.uploadInfo > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)'),
        'send_keys')
    element23 = ((By.CSS_SELECTOR, '.ml-20 > div:nth-child(1) > div:nth-child(2) > i:nth-child(1)'), 'click')
    element24 = ((By.CSS_SELECTOR, 'button.el-button--default:nth-child(2) > span:nth-child(1)'), 'click')
    element25 = ((By.CSS_SELECTOR, '[placeholder="请输入手机号"]'), 'send_keys')
    element26 = ((By.CSS_SELECTOR, 'button.btn > span:nth-child(1)'), 'click')
    element27 = ((By.CSS_SELECTOR, 'span.fr:nth-child(4)'),'click')
    element28 = ((By.CSS_SELECTOR, 'input.input:nth-child(3)'), 'send_keys')
    element29 = ((By.CSS_SELECTOR, 'button.btn:nth-child(2) > span:nth-child(1)'), 'click')
    element30 = (By.CSS_SELECTOR, ' .cardImgView > div> i:nth-child(1)')
    element31 = (By.CSS_SELECTOR, 'button.ml-20 > span:nth-child(1)')
    element32 = ((By.CSS_SELECTOR,
                  'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(3) > div.uploadInfo.clearfix.ml-30 > div.upload.fl.mt-20 > input'),
                 'send_keys')
    element33 = ((By.CSS_SELECTOR, 'div.uploadInfo:nth-child(1) > div:nth-child(1) > input:nth-child(2)'), 'send_keys')
    element34 = ((By.CSS_SELECTOR, 'div.uploadInfo:nth-child(2) > div:nth-child(1) > input:nth-child(2)'), 'send_keys')
    element35 = ((By.CSS_SELECTOR, '[placeholder="请选择政治面貌"]'), 'click')
    element36 = (By.XPATH, '/html/body/div[last()]/div[1]/div[1]/ul/li/span')
    element37 = ((By.CSS_SELECTOR, '[placeholder="请输入职业"]'), 'send_keys')
    element38 = ((By.CSS_SELECTOR, '[placeholder="请输入证件号码"]'), 'send_keys')
    element39 = ((By.CSS_SELECTOR, '[placeholder="请输入姓名"]'), 'send_keys')
    element40 = ((By.CSS_SELECTOR, '[placeholder="请选择出生日期"]'), 'click')
    element41 = (By.CSS_SELECTOR, 'span.el-date-picker__header-label:nth-child(3)')
    element42 = (By.CSS_SELECTOR, 'span.el-date-picker__header-label:nth-child(4)')
    element43 = ((By.CSS_SELECTOR, '[aria-label="前一年"]'), 'click')
    element44 = ((By.CSS_SELECTOR, '[aria-label="后一年"]'), 'click')
    element45 = ((By.CSS_SELECTOR, '[aria-label="上个月"]'), 'click')
    element46 = ((By.CSS_SELECTOR, '[aria-label="下个月"]'), 'click')
    element47 = (By.CSS_SELECTOR, '[class="available"] > div >span')
    element48 = (By.CSS_SELECTOR, 'button.mr-30 > span:nth-child(1)')
    element49 = (By.CSS_SELECTOR, 'button.buttonStyle > span')
    element50 = (
    (By.CSS_SELECTOR, 'div.item:nth-child(15) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)'), 'send_keys')
    element51 = (By.CSS_SELECTOR, 'div.item> label > span:nth-child(2) > span:nth-child(2)')
    element52 = ((By.CSS_SELECTOR, '[placeholder="身份证编号(必填)"]'), 'send_keys')
    element53 = ((By.CSS_SELECTOR, '[placeholder="请输入职业"]'), 'send_keys')
    element54 = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[5]/div[2]/div/label/span[2]')
    element55=((By.CSS_SELECTOR,'.el-message-box__btns > button > span:nth-child(1)'),'click')
