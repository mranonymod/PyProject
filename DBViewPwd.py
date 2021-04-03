from DBconnect import *

class viewShd:
    def __init__(self,username):
        self.db=mydb
        self.username=username
    def show(self):
        self.cur=self.db.cursor()
        self.cur.execute('''SELECT SharedID FROM SHDGRP WHERE Username = %s''',(self.username,))
        self.result2=self.cur.fetchone()[0]
        if(self.result2):
            return self.result2
        else:
            return False
    def getpwd(self):
        if(self.show()):
            self.cur1=self.db.cursor()
            self.cur1.execute('''SELECT Service,Passwords FROM Passwords WHERE SharedID = %s''',(self.result,))
            self.passervice=self.cur1.fetchone()
            return self.passervice
        else:
            return False
        self.db.close()

class viewPers: 
    def __init__(self,username):
        self.db=mydb
        self.username=username
    def find(self):
        self.cur1=self.db.cursor()
        self.cur1.execute('''SELECT * FROM Passwords WHERE EXISTS(SELECT Username FROM Passwords WHERE Username = %s) HAVING Username = %s''',(self.username,self.username))
        self.result=self.cur1.fetchall()
        if(self.result):
            return self.result
        else:
            return False


'''a=viewPers("bruh")
for row in a.find():
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])'''
    
    