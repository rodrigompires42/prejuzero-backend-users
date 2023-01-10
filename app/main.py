
import os
from os.path import join, dirname
from dotenv import load_dotenv

from fastapi import FastAPI

dotenv_path = join(dirname(dirname(__file__)), '.env')
load_dotenv(dotenv_path)

TRANSACTIONS_MICROSERVICE_PORT = os.environ.get("USERS_MICROSERVICE_PORT")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "users microservices"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}