from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app import models, schemas


def get_all(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No users found")

    return users
