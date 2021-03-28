from connect import *

def reg(self,username,name,email,password):
  self.db=mydb
  self.cur=self.db.cursor()
  self.cur.execute('''INSERT INTO Users VALUES(%s,%s,%s,%s)''',(username,name,email,password))
  self.db.commit()
  print(self.cur.rowcount, "record inserted.")

  self.db.close()

