from typing import List

from fastapi import APIRouter, Depends, status
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


@router.post("/", response_model=schemas.User, status_code=status.HTTP_202_ACCEPTED)
def create_user(
    request: schemas.User,
    db: Session = Depends(get_db)):
    return user_controller.create(request, db)


@router.delete("/", status_code=status.HTTP_200_OK)
def delete_user(id: int, db: Session = Depends(get_db)):
    user_controller.delete(id, db)


@router.get("/{id}", response_model=schemas.User, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_controller.show(id, db)


@router.put("/{id}", response_model=schemas.User, status_code=status.HTTP_200_OK)
def update_user(id: int, request: schemas.UserUpdate, db: Session = Depends(get_db)):
    return user_controller.update(id, request, db)