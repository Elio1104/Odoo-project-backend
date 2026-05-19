from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.dependencies import get_db
from schemas.employee import EmployeeRead, EmployeeCreate
from services import employee_service

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/create", response_model=EmployeeRead, status_code=201)
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    return employee_service.create_employee(db, data)

@router.get("/read/{employee_id}", response_model=EmployeeRead)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    return employee_service.read_employee(db, employee_id)