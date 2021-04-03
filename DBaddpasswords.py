from connect import *

class db:
    def __init__(self,username):
        self.username = username
        self.db=mydb
    def check(self,Service):
        self.cur2=self.db.cursor()
        self.service=Service
        self.cur2.execute('''(SELECT Services FROM ServicesR WHERE Services=%s)''',(self.service,))
        self.check1=self.cur2.fetchone()
        self.cur2.close()
        self.cur4=self.db.cursor()
        self.cur4.execute('''SELECT Service FROM Passwords WHERE Service=%s''',(self.service,))
        self.check2=self.cur4.fetchone()
        self.cur4.close()
        if(self.check1):
            return True
            if(self.check2):
                return False
            else:
                return True
        else:
            self.inService=self.db.cursor()
            self.inService.execute('''INSERT INTO ServicesR(Services) VALUES(%s)''',(self.service,))
            self.db.commit()
            self.inService.close()
            return True
        self.db.close()
    def add(self,AccUserName,EPassword,Service):
        self.AccUserName = AccUserName
        self.EPassword = EPassword
        self.Service = Service
        if(self.check(self.Service)):
            self.cur3=self.db.cursor()
            self.cur3.execute('''INSERT INTO Passwords(Username,AccUserName,Service,Passwords) VALUES(%s,%s,%s,%s)''',(self.username,self.AccUserName,self.Service,self.EPassword))
            self.db.commit()
            return True
        else:
            return
        self.db.close()
    def getServicesU(self):
        self.db=mydb
        self.cur1=self.db.cursor()
        self.cur1.execute('''SELECT Service from Passwords WHERE Username = %s''',(self.username,))
        self.services=self.cur1.fetchall()
        return self.services
        self.db.close()
    def getServices(self):
        self.db=mydb
        self.cur5=self.db.cursor()
        self.cur5.execute('''SELECT Services from ServicesR''')
        self.services=self.cur5.fetchall()
        self.cur5.close()
        return self.services
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