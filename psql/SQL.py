import pymysql
class NDDL(object):
    def Ndb(self , host ,user , password ,db):
        db = pymysql.connect(host = host,
                                  user = user,
                                  password = password,
                                  db = db)
        cursor = db.cursor()
        return cursor,db
    def Nselect(self,sql,host,user,password,db):
        cursor,_ = self.Ndb(host = host , user = user ,password = password ,db = db)
        _,db = self.Ndb(host = host , user = user ,password = password ,db = db)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            m = cursor.fetchall()
            kill = {}
            for i in m:
                list = []
                [list.append(str(n)) for n in i]
                kill[i[0]] = str(i[1])
        except:
            # 发生错误时回滚
            db.rollback()
            print("SQL有误")
            db.close()

        return kill
    def Update(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()
            print(sql+"SUCCESS")
        except:
            #self.db.rollback()
            self.db.close()
            print('*'*5+sql+"FAIL")