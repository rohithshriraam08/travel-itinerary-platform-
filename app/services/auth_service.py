from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return {"message": "User not found"}

    if user.password != password:
        return {"message": "Invalid password"}

    return {
        "message": "Login Successful",
        "user": user
    }