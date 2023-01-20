
import os
from os.path import join, dirname

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "users microservices"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    USERS = [
        {
            "id": 1,
            "name": "Rodrigo"
        },
        {
            "id": 2,
            "name": "Kaio"
        },
    ]
    user = next(user for user in USERS if user["id"] == user_id)
    return {"user_id": user_id, "user_name": user["name"]}
