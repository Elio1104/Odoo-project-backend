from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Departments
from repositories import department_repo
from schemas.department import DepartmentCreate, DepartmentUpdate


def create_department(db: Session, data: DepartmentCreate) -> Departments:
    department = department_repo.create_department(db, {
        'name': data.name,
        'description': data.description,
        'manager_id': data.manager_id
    })

    return department

def search_department(db: Session, **filters):
    return department_repo.search_departments(db, **filters)

def update_department(db: Session, department_id: int, data: DepartmentUpdate):
    payload = data.model_dump(exclude_none=True)
    department =  department_repo.update_department(db, department_id, payload)

    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")

    return department

def delete_department(db: Session, department_id: int):
    department = department_repo.delete_department(db, department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department