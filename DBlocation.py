from DBconnect import *
def loc(service):
    db=mydb
    cur4=db.cursor()
    cur4.execute('''SELECT * FROM ServicesR WHERE Services=%s''',(service,))
    check2=cur4.fetchone()
    cur4.close()
    website,signin,emailidp,passwordp,signinb=check2[2:]
    if(website):
        return website,signin,emailidp,passwordp,signinb
    else:
        return False
'''print(loc("NETFLIX"))'''