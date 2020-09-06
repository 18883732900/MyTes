from Base.number import number
from  Base.name import name
from Base.idCard import IdNumber
from  Base.Mysqldb import Mysqldb


idcard=IdNumber.generate_myid()
list =  Mysqldb().mysqldb_02(type=4,number=number(),title='%正确%')
login=Mysqldb().mysqldb(type=1)
select= Mysqldb().mysqldb(type=2)
worker_job= Mysqldb().mysqldb(type=3)
Brithday = Mysqldb().mysqldb(type=6)
user=Mysqldb().mysqldb_02(type=5, number="{0},{1}".format(IdNumber.generate_myid(),name()), title='%正确%')
file = r"C:\Users\26765\Desktop\python测试\Ui自动化\Data\微信截图_20200820115449.png"
shenfzz = r'C:\Users\26765\Desktop\python测试\Ui自动化\Data\身份证正面照片.jpg'
shenfzf = r'C:\Users\26765\Desktop\python测试\Ui自动化\Data\身份证反面照片.jpg'
file_path = [(shenfzz,shenfzf,'身份证'),(file,file,'其他')]
file_path1=[file,file,file,file]
Issue_permissions=Mysqldb().mysqldb_03(type=7)



if __name__ == '__main__':
    print(login[-1][0])


