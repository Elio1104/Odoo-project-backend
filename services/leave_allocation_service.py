from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories import leave_allocation_repo
from schemas.leave_allocation import LeaveAllocationCreate, LeaveAllocationUpdate

def create(db: Session, data: LeaveAllocationCreate):
    if leave_allocation_repo.get_existing(db, data.employee_id, data.leave_type_id, data.year):
        raise HTTPException(400, "Une allocation existe déjà pour cet employé / type / année")
    return leave_allocation_repo.create(db, data.model_dump())

def get_by_employee(db: Session, employee_id: int, year: int = None):
    return leave_allocation_repo.get_by_employee(db, employee_id, year)

def update(db: Session, allocation_id: int, data: LeaveAllocationUpdate):
    result = leave_allocation_repo.update(db, allocation_id, data.model_dump(exclude_none=True))
    if result is None:
        raise HTTPException(404, "Allocation non trouvée")
    return result