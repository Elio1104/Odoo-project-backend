from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories import leave_type_repo
from schemas.leave_type import LeaveTypeCreate, LeaveTypeUpdate

def create(db: Session, data: LeaveTypeCreate):
    return leave_type_repo.create(db, data.model_dump())

def get_all(db: Session):
    return leave_type_repo.get_all(db)

def update(db: Session, leave_type_id: int, data: LeaveTypeUpdate):
    result = leave_type_repo.update(db, leave_type_id, data.model_dump(exclude_none=True))
    if result is None:
        raise HTTPException(404, "Leave type non trouvé")
    return result