from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.auth.hashing import Hash


def get_all(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No users found")

    return users


def create(request: schemas.User, db: Session):
    request_dict = request.dict()

    user = db.query(models.User).filter(request_dict["email"] == models.User.email).all()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Email already in use")

    new_user = models.User(
        email=request.email,
        password=Hash.bcrypt(request.password),
        name=request.name,
        phone=request.phone
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    """Get user by id"""
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user


def update(id: int, request: schemas.UserUpdate, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    
    
    updated_user_dict = {
        "email":user.first().to_dict()["email"],
        "password":user.first().to_dict()["password"],
        "name":request.name,
        "phone":request.phone
    }

    user.update(updated_user_dict)
    db.commit()
    return user.first()
    



def delete(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    db.delete(user)
    db.commit()


