from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from app import schemas
from app.controllers import user_controller
from app.database import get_db


router = APIRouter(
    prefix="/api/v1/users",
    tags=["User"]
)


@router.get("/", response_model=List[schemas.User], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    return user_controller.get_all(db)
