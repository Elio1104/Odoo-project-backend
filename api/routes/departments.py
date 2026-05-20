from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependencies import get_db
from schemas.department import DepartmentRead, DepartmentCreate
from services import department_service

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.post("/create", response_model=DepartmentRead, status_code=201)
def create_department(data: DepartmentCreate, db: Session = Depends(get_db())):
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