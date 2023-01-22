from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models
from app.auth.hashing import Hash
from app.auth.jwt_token import create_access_token
from app.database import get_db

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/api/v1/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid credentials")

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")

    access_token = create_access_token(
        data={"id": user.id, "email": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}