import mysql.connector

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="passwordmanager"
    )
except mysql.connector.DataError as e:
    print("DataError")
    print(e)

except mysql.connector.InternalError as e:
    print("InternalError")
    print(e)

except mysql.connector.IntegrityError as e:
    print("IntegrityError")
    print(e)

except mysql.connector.OperationalError as e:
    print("OperationalError")
    print(e)

except mysql.connector.NotSupportedError as e:
    print("NotSupportedError")
    print(e)

except mysql.connector.ProgrammingError as e:
    print("ProgrammingError")
    print(e)

except :
    print("DB OFFLINE/Unknown error occurred")

