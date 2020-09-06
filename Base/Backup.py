import MySQLdb
from Data import  data_test01,data_test02

class Mysqldbbackup():
    def __init__(self):
        self.con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='test', charset='utf8')
        self.cursor = self.con.cursor()
    def backup_uesr(self):
        sql="INSERT INTO user(name, brithday,number, idcard, addr, Relationship_type, Issue_permissions,operator) VALUES (%s,%s,%s,%s,%s,%s,%s,%s); "
        self.cursor.execute(sql,(str(data_test02.user[-1][1]),"{0}年{1}月{2}日".format(data_test02.Brithday[-1][1],data_test02.Brithday[-1][2],data_test02.Brithday[-1][0])
                                 ,str(data_test02.list[-1])
                   ,str(data_test02.user[-1][0])
                   ,str(data_test02.select[-1])
              ,str( '%s,%s'%(data_test02.Relationship_type[-1][0],data_test02.Relationship_type[-1][1]))
                   ,str(data_test02.Issue_permissions[-1])
                   ,str(data_test02.login[-1][0])))
        self.con.commit()
        s=self.cursor.fetchall()
        return s

    def backup_worker(self):
        sql="INSERT INTO worker(name, brithday,number, idcard, addr, Relationship_type, Issue_permissions,operator) VALUES (%s,%s,%s,%s,%s,%s,%s,%s); "
        r=(data_test01.user[-1][1],
         "{0}年{1}月{2}日".format(data_test01.Brithday[-1][1], data_test01.Brithday[-1][2], data_test01.Brithday[-1][0])
         , data_test01.list[-1]
         , data_test01.user[-1][0]
         , data_test01.select[-1]
         , data_test01.worker_job[-1]
         , data_test01.Issue_permissions[-1]
         , data_test01.login[-1][0])
        # print(sql%r)
        self.cursor.execute(sql,(str(data_test01.user[-1][1]),"{0}年{1}月{2}日".format(data_test01.Brithday[-1][1],data_test01.Brithday[-1][2],data_test01.Brithday[-1][0])
                                 ,str(data_test01.list[-1])
                   ,str(data_test01.user[-1][0])
                   ,str(data_test01.select[-1])
              ,str(data_test01.worker_job[-1])
                   ,str(data_test01.Issue_permissions[-1])
                   ,str(data_test01.login[-1][0])))
        self.con.commit()
        s=self.cursor.fetchall()
        return s


if __name__ == '__main__':
    a=Mysqldbbackup().backup_uesr()
    print(a)