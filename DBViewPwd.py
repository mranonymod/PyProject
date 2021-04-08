from DBconnect import *

class viewShd:
    def __init__(self,username):
        self.db=mydb
        self.username=username
    def getPasses(self,viewu):
        """return encryption key(hashed pwd) and encrypted passwords

        Args:
            viewu (string): the username of user who wants to view passwords shared with him

        Returns:
            (list,string): ([(Username,Service,Password),...],Key)
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
        """get encryption key (main password (hashed))

        Args:
            id (List/Tuples): SharedID's coresponding to services 

        Returns:
            [List/Tuples]: SHA256 hashes password key for all coresponding Shared IDs used to encrypt the stored passwords 
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
    def getusers(self):
        """get users to whom passwords have been shared

        Returns:
            A list of tuple:[ (username,sharedid,services),...] 
        """
        self.users=[]
        self.ids=[]
        self.cur=self.db.cursor()
        self.services=[]
        self.cur.execute('''SELECT SharedID,Service FROM Passwords WHERE Username = %s''',(self.username,))
        for z in self.cur.fetchall():
            self.ids.append(z)
        self.cur.close()
        self.getuser=self.db.cursor()
        for x in self.ids:
            self.getuser.execute('''SELECT Username FROM SHDGRP WHERE SharedID = %s''',(x[0],))
            all=self.getuser.fetchall()
            for z in all:
                L=(z[0],x[0],x[1])
                self.users.append(L)
        return self.users
        
class viewPers: 
    def __init__(self,username):
        self.db=mydb
        self.username=username
    def find(self):
        """for displaying the stored passwords of a given user

        Returns:
            List of Tuples: Passwords stored and other details regarding it
        """
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
    print(row[5])
a=viewShd("bruh")
print(a.getusers())'''