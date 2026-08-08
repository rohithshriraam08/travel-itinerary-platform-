from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserCreate
from app.services.auth_service import create_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/")
def auth_home():
    return {"message": "Authentication Module"}

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    return login_user(db, email, password)