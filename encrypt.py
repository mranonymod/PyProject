import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):
    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = bytes.fromhex(key)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

# "bruh"====> sha256 hash===>hexadecimal===>"408f31d86c6bf4a8aff4ea682ad002278f8cb39dc5f37b53d343e63a61f3cc4f"

#abovementioned is how the password gets stored in the DB

# we get the stored key from the db and convert the hex into bytes since it's already hashed by sha256

#"408f31d86c6bf4a8aff4ea682ad002278f8cb39dc5f37b53d343e63a61f3cc4f" (hexadecimal sha256 hashed) 
#' b"@\x8f1\xd8lk\xf4\xa8\xaf\xf4\xeah*\xd0\x02'\x8f\x8c\xb3\x9d\xc5\xf3{S\xd3C\xe6:a\xf3\xccO" ' (bytes hexadecimal sha256 hashed)

#hex sha256 hashed to byte sha256 hashed by (bytes.fromhex(value))
#byte sha 256 hashed to hex sha256 hashed by (values.hex())

