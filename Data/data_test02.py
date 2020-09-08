from Base.number import number
from  Base.name import name
from Base.idCard import IdNumber
from  Base.Mysqldb import Mysqldb

file = r"C:\Users\26765\Desktop\python测试\Ui自动化\Data\微信截图_20200820115449.png"
shenfzz = r'C:\Users\26765\Desktop\python测试\Ui自动化\Data\身份证正面照片.jpg'
shenfzf = r'C:\Users\26765\Desktop\python测试\Ui自动化\Data\身份证反面照片.jpg'
file_list=[file,file]
file_path = [(shenfzz,shenfzf,file_list,2)]
file_path1=[file,file,file,shenfzz]
file_list4=[(file,),(file,file)]


login=Mysqldb().mysqldb(table='data_test02',type=1)
select=Mysqldb().mysqldb(table='data_test02',type=2)
lists =  Mysqldb().mysqldb_02(type=4,number=number(),title='%正确%',table='data_test02')
owner_message=Mysqldb().mysqldb_04(type=8,table='data_test02',name=name(),id=IdNumber.generate_myid(),number=number(),cnumber=number()[-1:-5:-1])
list=Mysqldb().mysqldb_02(type=4,number=number(),title='%正确%',table='data_test02')
file_path2 = [(shenfzz,shenfzf,'身份证'),(file,file,'其他')]
user=Mysqldb().mysqldb_02(type=5, number="{0},{1}".format(IdNumber.generate_myid(),name()), title='%正确%',table='data_test02')
Brithday = Mysqldb().mysqldb(type=6,table='data_test02')
Issue_permissions=Mysqldb().mysqldb_03(type=7,table='data_test02')
Relationship_type=Mysqldb().mysqldb(table='data_test02',type=9)
worker_job= Mysqldb().mysqldb(type=3,table='data_test02')









if __name__ == '__main__':
    print(Relationship_type)
