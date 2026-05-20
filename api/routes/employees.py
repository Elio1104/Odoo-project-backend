from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependencies import get_db
from schemas.employee import EmployeeRead, EmployeeCreate, EmployeeUpdate
from services import employee_service

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/create", response_model=EmployeeRead, status_code=201)
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        return employee_service.create_employee(db, data)
    except HTTPException as e:
        raise e

@router.get("/get", response_model=list[EmployeeRead])
def get_employee(
        employee_id: Optional[int] = None,
        email: Optional[str] = None,
        department_id: Optional[int] = None,
        role: Optional[str] = None,
        is_active: Optional[bool] = None,
        limit: Optional[int] = None,
        db: Session = Depends(get_db)
):
    return employee_service.search(
        db,
        employee_id=employee_id,
        email=email,
        department_id=department_id,
        role=role,
        is_active=is_active,
        limit=limit
)

@router.patch("/update/{employee_id}", response_model=EmployeeRead)
def update_employee(employee_id: int, data: EmployeeUpdate, db: Session = Depends(get_db)):
    return employee_service.update_employee(db, employee_id, data)

@router.delete("/delete/{employee_id}", response_model=EmployeeRead)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return employee_service.delete_employee(db, employee_id)