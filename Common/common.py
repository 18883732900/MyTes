import time

from Base.initdriver import  inidriver
from Base.name import name
from Base.idCard import IdNumber
from Base.number import number
from Common.uploda_worker import uploda
from Common.Resident_check_in import Resident_check


class Page(object):
  def __init__(self,driver):
          self.driver=driver

  def uploda(self):
      return  uploda(self.driver)

  def  Resident(self):
      return  Resident_check(self.driver)


if __name__ == '__main__':
    file = r"C:\Users\26765\Desktop\python测试\Ui自动化\Data\微信截图_20200820115449.png"
    shenfzz = r'C:\Users\26765\Desktop\python测试\Ui自动化\Data\身份证正面照片.jpg'
    shenfzf = r'C:\Users\26765\Desktop\python测试\Ui自动化\Data\身份证反面照片.jpg'
    list=[file,file]
    init=inidriver('http://test.bjhontai.com:180/#/login')
    init.maximize_window()
    c=Page(init).Resident()
    c.login('admin','123456')
    c.int('天坛社区','天坛小区','天坛东里','1单元','14','02')
    # c.owner(name(),IdNumber.generate_myid(),number(),number()[-1:-6:-1])
    # c.img(shenfzz,shenfzf,list,2)
    # time.sleep(2)
    # c.submin()

    c.cd_worker( number())
    c.up_worker(file)
    time.sleep(10)
    c.clickup()
    c.shengfz( file_path1=shenfzz, file_path2=shenfzf, type_cl='身份证')
    time.sleep(10)
    c.setup_idcard(IdNumber.generate_myid(),name())
    c.job('测试')
    time.sleep(3)
    c.selects_Political('群众')
    c.Relationship_type('常住','租客',[file,file])
    time.sleep(3)
    # c.Issue_permissions(('IC卡绑定','身份证绑定'),('温控门禁设备--61028','月坛小区门禁设备'),"18865572920","18988739264")
































