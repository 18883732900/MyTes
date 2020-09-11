import MySQLdb

class Mysqldb_test():
    def __init__(self):
        self.con = MySQLdb.connect(host='172.16.13.95', user='root', passwd='123456', db='aicity', charset='utf8')
        self.cursor = self.con.cursor()



    def  mysqldn_01(self,c,g,b,u,f,r):
        sql = "select uh.house_id,uh.user_id,uh.confirmation_status,uh.leave_status,uh.role,h.type,count(uh.house_id) c from user_house uh  LEFT JOIN house h on uh.house_id=h.id   where h.community_name like '%{0}%' and h.garden_name like '%{1}%' and h.building_name LIKE '%{2}%' and  h.unit_name like '%{3}%' and h.floor_name  like '%{4}%' and h.room_name like '%{5}%'  and uh.leave_status=0 AND uh.role=27 and uh.confirmation_status =2 GROUP BY uh.house_id  HAVING  c>type*2"
        s=self.cursor.execute(sql.format(c,g,b,u,f,r))
        sql2="select h.type from house h where h.community_name like '%{0}%' and h.garden_name like '%{1}%' and h.building_name LIKE '%{2}%' and h.unit_name like '%{3}%' and h.room_name like '%{4}%'"
        p=self.cursor.execute(sql2.format(c,g,b,u,r))
        mysql_data=self.cursor.fetchall()[0][0]
        list=[mysql_data,s]
        return list






if __name__ == '__main__':
    m=Mysqldb_test()
    v= m.mysqldn_01(c='天坛社区', g='天坛小区', b='天坛东里', u='1单元',f='14', r='02')
    print(v)
