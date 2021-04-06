from DBconnect import *

class shd:
    def __init__(self):
        self.db=mydb
    def show(self,addu):
        self.username1=addu
        self.cur=self.db.cursor()
        self.cur.execute('''SELECT Username FROM Users WHERE Username = %s''',(self.username1,))
        self.result=self.cur.fetchone()[0]
        self.cur.close()
        if(self.result):
            return True
        else:
            return False
    def share(self,username,sharedid,service):
        self.username=username
        self.sharedid=sharedid
        self.service=service
        if(self.show(self.username)):
            self.cur2=self.db.cursor()
            self.cur2.execute('''UPDATE Passwords SET SharedID=%s WHERE Service=%s AND SharedID IS NULL''',(self.sharedid,self.service))
            self.db.commit()
            if(self.cur2.rowcount):
                self.cur1=self.db.cursor()
                self.cur1.execute('''INSERT SHDGRP(SharedID,Username) VALUES (%s,%s)''',(self.sharedid,self.username))
                self.passervice=self.cur1.rowcount
                self.cur1.close()
                self.db.commit()
            else:
                self.cur6=self.db.cursor()
                self.cur6.execute('''SELECT SharedID FROM Passwords WHERE Service = %s''',(self.service,))
                self.id=self.cur6.fetchone()[0]
                self.cur1=self.db.cursor()
                self.cur1.execute('''INSERT SHDGRP(SharedID,Username) VALUES (%s,%s)''',(self.id,self.username))
                self.passervice=self.cur1.rowcount
                self.cur1.close()
                self.db.commit()
            return self.passervice
        else:
            return False
    def getPasses(self,viewu):
        self.username2=viewu
        self.r=[]
        self.cur2=self.db.cursor()
        self.cur2.execute('''SELECT SharedID FROM SHDGRP WHERE Username = %s''',(self.username2,))
        self.id=self.cur2.fetchall()
        if(self.id):
            self.k=self.givekey(self.id)
            for p in self.id:
                for q in p:
                    self.cur3=self.db.cursor()
                    self.cur3.execute('''Select Username,Service,Passwords FROM Passwords WHERE SharedID=%s''',(q,))
                    self.r.append(self.cur3.fetchall()[0])
            return self.r,self.k
        else:
            return False
        self.cur3.close()
    def givekey(self,id):
        self.id=id
        self.u=[]
        self.key=[]
        self.cur4=self.db.cursor()
        for x in self.id:
            for y in x:
                self.cur4.execute('''SELECT Username FROM Passwords WHERE SharedID=%s''',(y,))
                self.u.append(self.cur4.fetchone()[0])
        self.cur4.close()
        self.cur5=self.db.cursor()
        for a in self.u:
            self.cur5.execute('''SELECT Password FROM Users WHERE Username=%s''',(a,))
            self.key.append(self.cur5.fetchone()[0])
        self.cur5.close()
        return self.key
'''b=shd()
print(b.share("Eren","123456","WIFI"))'''

'''a=shd()
if(a.getPasses("bruh")):
    c,d=a.getPasses("bruh")
    print(c)
    print(d)
else:
    print('LOOOL')'''