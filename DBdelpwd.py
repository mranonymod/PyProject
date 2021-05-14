from DBconnect import *
from icecream import ic

class db1:
    def __init__(self,username,service):
        self.username = username
        self.service=service
        self.db=mydb
    def checksh(self):
        self.cur1=self.db.cursor()
        self.cur1.execute('''SELECT SharedID FROM SHDGRP WHERE SharedID=(SELECT SharedID FROM Passwords WHERE Service = %s AND Username = %s)''',(self.service,self.username))
        self.id=self.cur1.fetchone()
        if(self.id):
            return False
        else:
            return True
    def delete(self):
        if(self.checksh()):
            self.cur2=self.db.cursor()
            self.cur2.execute('''DELETE FROM Passwords WHERE Service = %s AND Username = %s''',(self.service,self.username))
            self.db.commit()
            self.id2=self.cur2.rowcount
            return self.id2
        else:
            return False
        
'''new=db1("bruh","DISNEY+")
print(new.delete())'''
