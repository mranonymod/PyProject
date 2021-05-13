from DBconnect import *

class shd:
    def __init__(self):
        self.db=mydb
    def qr1(self,username,service):
        self.cur7=self.db.cursor()
        self.cur7.execute('''SELECT SharedID FROM Passwords WHERE Username = %s AND Service =%s''',(username,service))
        self.result=self.cur7.fetchone()
        self.cur7.close()
        return self.result[0]
    def show(self,addu):
        """Check if username exists in DB before sharing password with it

        Args:
            addu (string): username

        Returns:
            Boolean: True if username found
        """
        self.username1=addu
        self.cur=self.db.cursor()
        self.cur.execute('''SELECT Username FROM Users WHERE Username = %s''',(self.username1,))
        self.result=self.cur.fetchone()
        self.cur.close()
        if(self.result):
            return True
        else:
            return False
    def share(self,user1,user2,service):
        """Stores the user id (with whom password is to be shared) and shared id in a seperate table so that

        Args:
            user1 (string): Username whose password is to be shared
            user2 (string): Username to whom password is going to be shared
            service (string): Account name of the password

        Returns:
            Int/Boolean: returns value of rows affected by insertion or False when sharing operation fails
        """
        self.username=user2
        self.user1=user1
        self.service=service
        if(self.show(self.username)):
            self.cur1=self.db.cursor()
            self.cur1.execute('''SELECT SharedID FROM Passwords WHERE Service = %s AND Username = %s''',(self.service,self.user1))
            self.id=self.cur1.fetchone()[0]
            if(self.check1(self.id,self.username)):
                self.cur6=self.db.cursor()
                self.cur6.execute('''INSERT SHDGRP(SharedID,Username) VALUES (%s,%s)''',(self.id,self.username))
                self.passervice=self.cur6.rowcount
                self.cur1.close()
                self.db.commit()
                return self.passervice
            else:
                return False
        else:
            return False
    def check1(self,id,usr):
        """checks if any passwords have already been shared to a given user id

        Args:
            id (string): SharedID assigned to a password that allows sharing
            usr (string): Username

        Returns:
                Boolean: False if any passwords have already been shared else True
        """
        self.chk=self.db.cursor()
        self.chk.execute('''SELECT SharedID,Username FROM SHDGRP WHERE SharedID=%s AND Username=%s''',(id,usr))
        self.r=self.chk.fetchall()
        if(self.r):
            return False
        else:
            return True
    def unshare(self,user1,user2,service):
        """removes the user id from the seperate table so as to revoke his access to shared password

        Args:
            user1 (string): Username whose password is to be unshared
            user2 (string): Username to whom password is going to be unshared
            service (string): Account name of the password

        Returns:
            Int/Boolean: returns value of rows affected by deletion or False when unsharing operation fails
        """
        self.username=user2
        self.user1=user1
        self.service=service
        if(self.show(self.username)):
            self.cur1=self.db.cursor()
            self.cur1.execute('''SELECT SharedID FROM Passwords WHERE Service = %s AND Username = %s''',(self.service,self.user1))
            self.id=self.cur1.fetchone()[0]
            self.cur6=self.db.cursor()
            self.cur6.execute('''DELETE FROM SHDGRP WHERE SharedID=%s AND Username=%s''',(self.id,self.username))
            self.passervice=self.cur6.rowcount
            self.cur1.close()
            self.db.commit()
            return self.passervice
        else:
            return False
    def getPasses(self,viewu):
        """return encryption key(hashed pwd) and encrypted passwords

        Args:
            viewu (string): username whose passswords are to be retrieved

        Returns:
            [type]: [description]
        """
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
        """get encryption key (main password (hashed)) by retrieving the username of the owner of passwords and then the password with the help of username

        Args:
            id (string): SharedID of the password 

        Returns:
            string: SHA256 Hashed password key of the user account
        """
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
    def chqr(self,shdid,usr):
        self.cur9=self.db.cursor()
        self.cur9.execute('''SELECT Username FROM Passwords WHERE SharedID = %s AND Username = %s''',(shdid,usr))
        self.rr=self.cur9.fetchone()
        return self.rr

    def qrsh(self,shdid,usr):
        if(self.chqr(shdid,usr)):
            return False
        else:
            self.cur9=self.db.cursor()
            self.cur9.execute('''INSERT INTO SHDGRP(SharedID,Username) VALUES(%s,%s)''',(shdid,usr))
            self.rr=self.cur9.rowcount
            self.db.commit()
            self.cur9.close()
            return self.rr

'''b=shd()
print(b.qrsh("63hWc7S#Te3v6iU4v","bruh"))'''

'''a=shd()
if(a.getPasses("bruh")):
    c,d=a.getPasses("bruh")
    print(c)
    print(d)
else:
    print('LOOOL')'''