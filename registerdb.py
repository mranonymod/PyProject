from connect import *
from app import Controller

class Reg():
  def __init__(self,username,name,email,password):
    self.username = username
    self.password=password
    self.username=username
    self.email = email
    self.name=name
  def insert(self):
    self.db=mydb
    self.cur=self.db.cursor()
    self.cur.execute('''INSERT INTO Users VALUES(%s,%s,%s,%s)''',(self.username,self.name,self.email,self.password))
    self.db.commit()
    print(self.cur.rowcount, "record inserted.")
    return self.cur.rowcount
    self.db.close()