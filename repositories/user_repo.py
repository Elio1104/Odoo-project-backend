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