from sqlalchemy.orm import Session

from models import Departments
from repositories import department_repo
from schemas.department import DepartmentCreate


def create_department(db: Session, data: DepartmentCreate) -> Departments:
    department = department_repo.create_department(db, {
        'name': data.name,
        'description': data.description,
        'manager_id': data.manager_id
    })

    return department

def search_department(db: Session, **filters):
    return department_repo.search_departments(db, **filters)
