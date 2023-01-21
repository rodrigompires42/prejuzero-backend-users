from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    phone: str

    class Config():
        orm_mode = True

class UserUpdate(BaseModel):
    name: str
    phone: str

    class Config():
        orm_mode = True