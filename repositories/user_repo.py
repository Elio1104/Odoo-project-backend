from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user import Users


def create_user(db: Session, user_data: dict):
    user = Users(
        email=user_data['email'],
        hashed_password=user_data['hashed_password'],
        role=user_data['role']
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_id(db: Session, user_id: int):
    stmt = select(Users).where(Users.id == user_id)
    result = db.execute(stmt).scalars().one_or_none()

    return result

def get_user_by_email(db: Session, email: str):
    stmt = select(Users).where(Users.email == email)
    result = db.execute(stmt).scalars().one_or_none()

    return result