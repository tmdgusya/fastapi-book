from passlib.context import CryptContext

class Crypto:

    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def encrypt(self, secret):
        return self.pwd_context.hash(secret=secret)
    
    def verify(self, secret, hash):
        return self.pwd_context.verify(secret=secret, hash=hash)