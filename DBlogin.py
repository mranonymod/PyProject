from DBconnect import *

class getdbpwd:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def check(self):
        self.db=mydb
        self.cur=self.db.cursor()
        check=(self.username,self.password)
        self.cur.execute("""SELECT * FROM Users WHERE Username = %s and Password=%s ;""",check)
        self.result=self.cur.fetchone()
        if(self.result):
            return True
        else:
            return False

        self.db.close()