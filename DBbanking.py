from DBconnect import *
class bdb:
    def __init__(self,username):
        self.username = username
        self.db=mydb
    def add(self,bname,custid,lgnpwd,txnpwd):
        self.cur=self.db.cursor()
        if(self.check1(custid)):
            return False
        else:
            self.cur.execute('''INSERT INTO BANK VALUES (%s,%s,%s,%s,%s)''',(self.username,bname,custid,lgnpwd,txnpwd))
            self.r=self.cur.rowcount
            self.db.commit()
            return self.r
    def check1(self,custid):
        self.cur1=self.db.cursor()
        self.cur1.execute('''SELECT CustomerID FROM BANK WHERE CustomerID=%s''',(custid,))
        self.z=self.cur1.fetchone()
        return self.z
    def view1(self):
        self.cur2=self.db.cursor()
        self.cur2.execute('''SELECT * FROM BANK WHERE Username=%s''',(self.username,))
        self.z=self.cur2.fetchall()
        return self.z
    def delete(self,custid):
        self.cur3=self.db.cursor()
        self.cur3.execute('''DELETE FROM BANK WHERE CustomerID=%s''',(custid,))
        self.r2=self.cur3.rowcount
        self.db.commit()
        return self.r2

'''b=bdb('bruh')
print(b.add("hi1","hi2","hi3","hi4"))
print(b.view1("bruh"))
print(b.delete("hi2"))
'''
