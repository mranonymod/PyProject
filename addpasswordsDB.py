from connect import *

class db:
    def __init__(self,username):
        self.username = username
        self.db=mydb
    def check(self,Service):
        self.cur2=self.db.cursor()
        self.cur2.execute('''INSERT INTO ServicesR(Services) VALUES(%s) WHERE NOT EXISTS(SELECT Services FROM ServicesR WHERE Services=%s)''',(self.Service,self.Service))
        self.db.commit()
        self.cur4=self.db.cursor()
        self.cur4.execute('''SELECT Service FROM Passwords WHERE Service=%s''',(self.Service,))

        if(self.cur2.rowcount):
            return True
        elif(self.cur4.rowcount):
            return False
        else:
            return True
        self.db.close()
    def add(self,AccUserName,EPassword,Service):
        self.AccUserName = AccUserName
        self.EPassword = EPassword
        self.Service = Service
        if(self.check):
            self.cur3=self.db.cursor()
            self.cur3.execute('''INSERT INTO Passwords(Username,AccUserName,Service,Passwords) VALUES(%s,%s,%s,%s)''',(self.username,self.AccUserName,self.Service,self.EPassword))
            self.db.commit()
            return True
        else:
            return
        self.db.close()
    def getkey(self):
        self.db=mydb
        self.cur=self.db.cursor()
        self.cur.execute('''SELECT Password from Users WHERE Username = %s''',(self.username,))
        self.result=self.cur.fetchall()[0][0]
        return self.result
        self.db.close()

# extract , is not an error (TUPLES ARE PASSED AS ARGUMENTS)
#[m][n] to get a specific cell from fetched data