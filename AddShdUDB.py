from connect import *

class add:
    def __init__(self,username):
        self.db=mydb
        self.username=username
    def show(self):
        self.cur=self.db.cursor()
        self.cur.execute('''SELECT Username FROM Users WHERE Username = %s''',(self.username,))
        self.result=self.cur.fetchone()[0]
        if(self.result):
            return True
        else:
            return False
    def share(self):
        if(self.show()):
            self.cur1=self.db.cursor()
            self.cur1.execute('''INSERT SHDGRP(SharedID,Username) VALUES (%s,%s)''',(self.sharedid,self.result))
            self.passervice=self.cur1.fetchone()
            return self.passervice

a=add("bruh")

print(a.share())