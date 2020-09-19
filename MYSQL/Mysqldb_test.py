import MySQLdb

class Mysqldb_test():

    def __init__(self,c,g,b,u,f,r):
        self.con = MySQLdb.connect(host='172.16.13.95', user='root', passwd='123456', db='aicity', charset='utf8')
        self.cursor = self.con.cursor()
        self.c=c
        self.g=g
        self.b=b
        self.u=u
        self.f=f
        self.r=r



    def  mysqldn_01(self):
        sql = "select uh.house_id,uh.user_id,uh.confirmation_status,uh.leave_status,uh.role,h.type,count(uh.house_id) c from user_house uh  LEFT JOIN house h on uh.house_id=h.id   where h.community_name like '%{0}%' and h.garden_name like '%{1}%' and h.building_name LIKE '%{2}%' and  h.unit_name like '%{3}%' and h.floor_name  like '%{4}%' and h.room_name like '%{5}%'  and uh.leave_status=0 AND uh.role=27 and uh.confirmation_status =2 GROUP BY uh.house_id  HAVING  c>type*2"
        # s是 超员数据1表示有
        s=self.cursor.execute(sql.format(self.c,self.g,self.b,self.u,self.f,self.r))
        sql2="select h.type,h.garden_id from house h where h.community_name like '%{0}%' and h.garden_name like '%{1}%' and h.building_name LIKE '%{2}%' and h.unit_name like '%{3}%' and h.floor_name like '%{4}%'  and h.room_name like '%{5}%'"
        self.cursor.execute(sql2.format(self.c,self.g,self.b,self.u,self.f,self.r))
        # room_type 是
        room_type=self.cursor.fetchall()[0]
        self.garand_id=room_type[1]
        list=[*room_type,s]
        return list

    @classmethod
    def  mysqldn_02(cls,c,g,b,u,f,r):
        f=cls(c,g,b,u,f,r)
        s=f.mysqldn_01()[1]
        print(s)
        sql="select device_name from user_face_device_info where garden_id={0} and is_del=0"
        f.cursor.execute(sql.format(s))
        a= f.cursor.fetchall()
        list=[]
        for i in a:
            list.append(i[0])
        return list





if __name__ == '__main__':
    c=Mysqldb_test.mysqldn_02(c='天坛社区', g='天坛小区', b='天坛东里', u='1单元',f='14', r='02')
    print(c)
