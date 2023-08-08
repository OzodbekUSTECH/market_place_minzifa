from passlib.context import CryptContext
import string
import random



class PasswordHandler:
    pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto",
    )

    @staticmethod
    def hash(password: str):
        return PasswordHandler.pwd_context.hash(password)

    @staticmethod
    def verify(plain_password, hashed_password):
        return PasswordHandler.pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def generate_password(length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))