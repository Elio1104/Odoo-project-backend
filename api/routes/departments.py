from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependencies import get_db
from schemas.department import DepartmentRead, DepartmentCreate, DepartmentUpdate
from services import department_service

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.post("/create", response_model=DepartmentRead, status_code=201)
def create_department(data: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        return department_service.create_department(db, data)
    except HTTPException as e:
        raise e

@router.get("/get", response_model=list[DepartmentRead])
def get_department(
        department_id: Optional[int] = None,
        department_name: Optional[str] = None,
        manager_id: Optional[int] = None,
        limit: Optional[int] = None,
        db: Session = Depends(get_db)
):
    return department_service.search_department(
        db,
        department_id=department_id,
        department_name=department_name,
        manager_id=manager_id,
        limit=limit
    )

@router.patch("/update/{department_id}", response_model=DepartmentRead)
def update_department(department_id: int, data: DepartmentUpdate, db: Session = Depends(get_db)):
    return department_service.update_department(db, department_id, data)

@router.delete("/delete/{department_id}", response_model=DepartmentRead)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    return department_service.delete_department(db, department_id)
