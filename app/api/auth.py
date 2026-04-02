from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.security import create_access_token
from app.schemas.user import UserCreate, UserLogin
from app.services.user_service import create_user, authenticate_user


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(db, user_data.email, user_data.password)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")

    return {"message": "User created"}


@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_data.email, user_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})
    return {"access_token": token}