from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import LeaveTypes


def create(db: Session, data: dict) -> LeaveTypes:
    leave_type = LeaveTypes(**data)
    db.add(leave_type)
    db.commit()
    db.refresh(leave_type)
    return leave_type

def get_by_id(db: Session, leave_type_id: int) -> Optional[LeaveTypes]:
    stmt = select(LeaveTypes).where(LeaveTypes.id == leave_type_id)
    result = db.execute(stmt).scalars().one_or_none()
    return result

def get_all(db: Session) -> list[LeaveTypes]:
    stmt = select(LeaveTypes)
    result = db.execute(stmt).scalars().all()
    return result

def update(db: Session, leave_type_id: int, data: dict) -> Optional[LeaveTypes]:
    leave_type = get_by_id(db, leave_type_id)
    if leave_type is None:
        return None
    for key, value in data.items():
        setattr(leave_type, key, value)
    db.commit()
    db.refresh(leave_type)
    return leave_type




