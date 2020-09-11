import MySQLdb
from Base.Make_date.idCard import IdNumber
from Base.Make_date.name import name
from Base.Make_date.number import number


class Mysqldb():
    def __init__(self):
        self.con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='test', charset='utf8')
        self.cursor = self.con.cursor()



    def mysqldb(self, type, table='data_test01'):
        sql = "select date_01 from {0} where type={1} ;"
        self.cursor.execute(sql.format(table, type))
        mysql_data = self.cursor.fetchall()
        list = []
        for i in mysql_data:
            s = i[0].split(',')
            list.append(tuple(s))
        self.cursor.close()
        return list




    def mysqldb_02(self, type, number, title, table="data_test01"):
        if type == 4:
            sq11 = "update {0} set date_01=%s where title like %s and type=%s"
            self.cursor.execute(sq11.format(table), (number, title, type))
        elif type == 5 :
            sq11 = "update {0} set date_01=%s where title like %s and type=%s"
            self.cursor.execute(sq11.format(table), (number, title, type))
        self.con.commit()
        sql2 = "select date_01 from {0} where type=%s;"
        self.cursor.execute(sql2.format(table), (type,))

        mysql_data = self.cursor.fetchall()
        list = []
        if type == 5 :
            for i in mysql_data:
                s = i[0].split(',')
                list.append(tuple(s))
        elif type == 4:
            for i in mysql_data:
                s = i[0]
                list.append(s)
        self.cursor.close()
        return list




    def mysqldb_03(self, type, table='data_test01'):
        sql3 = 'select substring_index(date_01,"|",-2 ) from {0} where type ={1}'
        self.cursor.execute(sql3.format(table,type))
        z = self.cursor.fetchall()
        y = z[0][0]
        sql2 ="UPDATE {0} SET date_01 = replace(date_01,%s,%s)  where type =%s"
        self.cursor.execute(sql2.format(table,),("%s"%y,'%s|%s'%(number(),number()),type))
        self.con.commit()
        sql = "select date_01 from %s where type=%d;"
        self.cursor.execute(sql % (table, type))
        mysql_data = self.cursor.fetchall()
        list = []

        for i in mysql_data:
            s = i[0].split("|")
            tunl = []
            for a in s:
                if ',' in a:
                    c = a.split(',')
                    tunl.append(c)
                else:
                    tunl.append(a)
            list.append(tuple(tunl))
        return list



    def mysqldb_04(self, type, name,id,number,cnumber,table='data_test01'):
        sql="update {0} set date_01 ='{2},{3},{4},{5}' where type={1}"
        self.cursor.execute(sql.format(table,type,name,id,number,cnumber))
        self.cursor.connection.commit()
        sql2="select date_01 from {0} where type ={1}"
        self.cursor.execute(sql2.format(table,type))
        s=self.cursor.fetchall()
        list=[]
        for i in s:
            li=i[0].split(",")
            list.append(tuple(li))
        return list



if __name__ == '__main__':
    # list = Mysqldb().mysqldb_02(type=4, number=number(), title='%正确%')
    # print(list)
    list = Mysqldb().mysqldb_04(type=5,table='data_test02',name=name(),id=IdNumber.generate_myid(),number=number(),cnumber=number()[-1:-5:-1])
    print(list)

