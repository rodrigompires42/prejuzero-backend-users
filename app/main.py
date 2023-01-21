
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users

app = FastAPI(
    title="PrejuZero Users Microservice"
)

app.include_router(users.router)
