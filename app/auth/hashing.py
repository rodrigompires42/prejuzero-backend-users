"""Hashing class"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    """Hash class"""

    @staticmethod
    def bcrypt(password: str):
        """Returns encrypted password"""
        return pwd_context.hash(password)

    @staticmethod
    def verify(plain_password, hashed_password):
        """Verify if string is equal to encrypted password"""
        return pwd_context.verify(plain_password, hashed_password)
