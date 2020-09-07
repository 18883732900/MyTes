from selenium.webdriver.common.by import By
class test01:
    element1 = (By.CSS_SELECTOR, '.el-message__content')

    '''定位手机号错误提示'''
    element3 = (By.CSS_SELECTOR,
                'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > div.el-row > div:nth-child(1) > form > div > div > div.el-form-item__error')
    '''定位信息界面进入后的标签定位'''
    element4 = (By.CSS_SELECTOR,
                'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(2) > button:nth-child(4) > span')
    '''定位手机号输入框'''
    element5 = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
    '''判断是否成功进入输入手机号界面'''
    element6 = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__header > span')
    '''提交空后的错误提示'''
    element7 = (By.XPATH, '/html/body/div[7]/p')

    element8 = (By.CSS_SELECTOR, '.mr-30 > div > div:nth-child(1) > img:nth-child(1)')

    '''定位身份证反面错误提示'''
    element9 = (By.XPATH, '/html/body/div[7]/p')
    '''定位身份证正面照片是否上传成功'''
    element10 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/img')
    '''定位身份证正反面照片是否上传成功'''
    element11 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/img')
    '''定位证件照片是否上传成功'''
    element12 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div[1]/div[2]/div/div[1]/img')
    '''定位打开摄像头按钮'''
    element13 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/button/span')

    element14 = (By.CSS_SELECTOR, '.el-message__content')
    element15 = (By.CSS_SELECTOR, '.el-form-item__error')

    element16 = (By.CSS_SELECTOR, 'div.uploadInfo:nth-child(2) > div:nth-child(1) > input:nth-child(2)')
    element17 = (By.CSS_SELECTOR, 'div.uploadInfo:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
    element18 = (By.CSS_SELECTOR, 'div.uploadInfo:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
    element19 = (By.CSS_SELECTOR, 'li.clearfix > span')
    element20 = (By.CSS_SELECTOR, '.baseCont > h3:nth-child(1)')
    element21 = (By.CSS_SELECTOR, 'label.el-checkbox.is-checked > span:nth-child(2)')
    element22 = (By.CSS_SELECTOR,
                 '.el-menu-vertical-demo > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > div:nth-child(1) > div:nth-child(4) > li:nth-child(1) > ul:nth-child(2) > div:nth-child(1) > div > li:nth-child(1) > span:nth-child(2)')
    element23 = (By.CSS_SELECTOR, '.el-message__content')


class test02():
    element1 = (By.CSS_SELECTOR, '.el-message__content')
    element2= (By.XPATH,'//*[@id="indexContent"]/section/main/div/div[2]/div/div/div[2]/h2')
    element3=(By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
    element4=(By.CSS_SELECTOR,
                'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > div.el-row > div:nth-child(1) > form > div > div > div.el-form-item__error')
    element5=(By.CSS_SELECTOR,
                'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div:nth-child(2) > button:nth-child(4) > span')
    element6=(By.CSS_SELECTOR, '.el-message__content')
    element7 = (By.XPATH, '/html/body/div[7]/p')
    element8 = (By.CSS_SELECTOR, 'div.uploadInfo:nth-child(2) > div:nth-child(1) > input:nth-child(2)')
    element9 = (By.CSS_SELECTOR, 'div.uploadInfo:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
    element10 = (By.CSS_SELECTOR, 'div.uploadInfo:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
    element11 = (By.CSS_SELECTOR, 'div.uploadInfo:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)')
    element12=(By.CSS_SELECTOR,'.res-info > div:nth-child(1) > div> div:nth-child(1) > img:nth-child(1)')
    element13 = (By.CSS_SELECTOR, '.el-form-item__error')
    element14= ((By.CSS_SELECTOR, '[placeholder="请选择出生日期"]'), 'move_to_element')
    element15=(By.CSS_SELECTOR, 'div.contractImgView> div:nth-child(2)')
    element16=((By.CSS_SELECTOR, 'div.contractImgView:nth-child(1) > div:nth-child(2)'), 'click')
    element17=((By.CSS_SELECTOR, '.el-message-box__btns > button:nth-child(2) > span:nth-child(1)'), 'click')

