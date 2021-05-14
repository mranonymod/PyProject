from DBconnect import *
from app import Controller

class Reg():
  def __init__(self,username,name,email,password):
    """ 
    Args:
        username (STRING): Username of User of Protekt
        name (STRING): Name of User of Protekt
        email (STRING): Email of User of Protekt
        password (STRING): Password of User of Protekt
    """
    self.db=mydb
    self.username = username
    self.password=password
    self.username=username
    self.email = email
    self.name=name
  def check(self):
    """verifies whether username is already in database

    Returns:
        Bool: True if registration is successful , else False.
    """
    self.cur2=self.db.cursor()
    self.cur2.execute('''SELECT Username FROM Users WHERE Username=%s''',(self.username,))
    self.result=self.cur2.fetchone()
    if(self.result):
        return False
    else:
        return True
    self.db.close()
  def insert(self):
    """executes sql query to insert user into database

    Returns:
        Bool:True if successful else False
    """
    if(self.check()):
      self.cur=self.db.cursor()
      self.cur.execute('''INSERT INTO Users VALUES(%s,%s,%s,%s)''',(self.username,self.name,self.email,self.password))
      self.db.commit()
      return True
    else:
      return False
    self.db.close()