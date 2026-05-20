from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.dependencies import get_db
from schemas.leave_type import LeaveTypeCreate, LeaveTypeRead, LeaveTypeUpdate
from services import leave_type_service

router = APIRouter(prefix="/leave-types", tags=["Leave Types"])

@router.post("/create", response_model=LeaveTypeRead, status_code=201)
def create(data: LeaveTypeCreate, db: Session = Depends(get_db)):
    return leave_type_service.create(db, data)

@router.get("/get", response_model=list[LeaveTypeRead])
def get_all(db: Session = Depends(get_db)):
    return leave_type_service.get_all(db)

@router.patch("/update/{leave_type_id}", response_model=LeaveTypeRead)
def update(leave_type_id: int, data: LeaveTypeUpdate, db: Session = Depends(get_db)):
    return leave_type_service.update(db, leave_type_id, data)