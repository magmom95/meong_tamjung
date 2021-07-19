import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                    user='root',
                                    password='1234',
                                    db = 'meong_tamjung',
                                    charset= 'utf-8')
        # 디폴트 Array based cursor는 Row의 결과값을 배열로 (PyMyMsql에서 정확히는 튜플) 리턴하는데, 
        # cursor 생성시 DictCursor 옵션을 주면, Row 결과를 Dictionary 형태로 리턴한다.
        # http://pythonstudy.xyz/python/article/202-MySQL-%EC%BF%BC%EB%A6%AC
        self.cursor(self.db.cursor(pymysql.cursor.DictCursor))

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row
    
    def commit(self):
        self.db.commit()

class Database2():
    # def insertdb(data):
    def insertdb():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
        cursor = conn.cursor()
        # cursor.execute("INSERT INTO user(id, pw, name, email) VALUES ('tjsdud594', '1234@', '룬선영', 'fbtjsdud594@gmail.com')", data)
        cursor.execute("INSERT INTO user(id, pw, name, email) VALUES ('tjsdud594', '1234@', '룬선영', 'fbtjsdud594@gmail.com')")
        print('완료')
        conn.commit()
        conn.close()

    def deletedb():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
        cursor = conn.cursor()
        cursor.execute("delete from user where name='룬선영'")
        print('완료')
        conn.commit()
        conn.close()

    def selectdb():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='meong_tamjung', charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select * from user")
        rows = cursor.fetchall()
        print(rows)
        conn.close()


# if __name__=="__main__":
#     # -*- conding: utf-8 -*-
    # Database2.deletedb()
    # Database2.insertdb()
    # Database2.selectdb()