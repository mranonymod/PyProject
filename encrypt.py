import hashlib

tempp="bruh"
class enc:
    def __init__(self,str):
        self.temp=str
    def hashit(self,str):
        str=hashlib.sha256(str.encode())
        pwd = str.hexdigest()
        return pwd
    def check(self):
        if self.hashit(tempp)==self.hashit(self.temp):
            print('bete moj kr di')
        else:
            print('＞︿＜')
