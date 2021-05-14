from DBconnect import *
def loc(service):
    """ returns the xpaths of the service for autologin

    Args:
        service (STRING): Service for which autologin function has been called

    Returns:
        Tuple/bool: Returns tuple consisting of xpaths of the service or returns False if service doesn't support autologin    """
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