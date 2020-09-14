import os
from Base.Make_date.name import name
from Base.Make_date.number import number
from Base.Make_date.idCard import IdNumber
from Base.MYSQL.Mysqldb import Mysqldb

idcard = IdNumber.generate_myid()

path__1 = os.path.join(os.getcwd(),'Image')
# path__1=r"C:\Users\26765\Desktop\python测试\Ui自动化\Image"


def path(file_name):
    path1 = os.path.join(path__1, file_name)
    return path1

s = os.walk(path__1)
for a, b, c in s:
    listt = [i for i in c]

file = path(listt[0])
shenfzz = path(listt[2])
shenfzf = path(listt[1])
file_path = [(shenfzz, shenfzf, '身份证'), (file, file, '其他')]
file_path1 = [file, file, file, file]


list = Mysqldb().mysqldb_02(type=4, number=number(), title='%正确%')
login = Mysqldb().mysqldb(type=1)
select = Mysqldb().mysqldb(type=2)
worker_job = Mysqldb().mysqldb(type=3)
Brithday = Mysqldb().mysqldb(type=6)
user = Mysqldb().mysqldb_02(type=5, number="{0},{1}".format(IdNumber.generate_myid(), name()), title='%正确%')
Issue_permissions = Mysqldb().mysqldb_03(type=7)





if __name__ == '__main__':
    print(user)
