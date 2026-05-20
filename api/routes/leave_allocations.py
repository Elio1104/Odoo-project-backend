from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.dependencies import get_db
from schemas.leave_allocation import LeaveAllocationCreate, LeaveAllocationRead, LeaveAllocationUpdate
from services import leave_allocation_service

router = APIRouter(prefix="/leave-allocations", tags=["Leave Allocations"])

@router.post("/create", response_model=LeaveAllocationRead, status_code=201)
def create(data: LeaveAllocationCreate, db: Session = Depends(get_db)):
    return leave_allocation_service.create(db, data)

@router.get("/employee/{employee_id}", response_model=list[LeaveAllocationRead])
def get_by_employee(employee_id: int, year: Optional[int] = None, db: Session = Depends(get_db)):
    return leave_allocation_service.get_by_employee(db, employee_id, year)

@router.patch("/update/{allocation_id}", response_model=LeaveAllocationRead)
def update(allocation_id: int, data: LeaveAllocationUpdate, db: Session = Depends(get_db)):
    return leave_allocation_service.update(db, allocation_id, data)