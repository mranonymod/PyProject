import hashlib 

def hashit(str1):
    str1=hashlib.sha256(str1.encode())
    pwd = str1.hexdigest()
    return pwd
