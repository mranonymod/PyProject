from connect import *

class db:
    def __init__(self,username):
        self.username = username
    def add(self,AccUserName,EPassword,Service):
        self.AccUserName = AccUserName
        self.EPassword = EPassword
        self.Service = Service
        self.db=mydb
        self.cur2=self.db.cursor()
        self.cur2.execute('''INSERT INTO ServicesR(Services) VALUES(%s)''',(self.Service,))
        self.db.commit()
        self.cur3=self.db.cursor()
        self.cur3.execute('''INSERT INTO Passwords(Username,AccUserName,Service,Passwords) VALUES(%s,%s,%s,%s)''',(self.username,self.AccUserName,self.Service,self.EPassword))
        self.db.commit()
        print(self.cur2.rowcount, "record inserted.")
        print(self.cur3.rowcount, "record inserted.")
        return
        self.db.close()
    def getkey(self):
        self.db=mydb
        self.cur=self.db.cursor()
        self.cur.execute('''SELECT Password from Users WHERE Username = %s''',(self.username,))
        self.result=self.cur.fetchall()[0][0]
        return self.result
        self.db.close()