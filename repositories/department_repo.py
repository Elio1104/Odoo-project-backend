from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.department import Departments

def create_department(db: Session, department_data: dict):
    department = Departments(
        name=department_data['name'],
        description=department_data['description'],
        manager_id=department_data['manager_id']
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    return department

def get_department_by_id(db: Session, department_id: int):
    stmt = select(Departments).where(Departments.id == department_id)
    result = db.execute(stmt).scalars().one_or_none()

    return result

def search_departments(
        db: Session,
        department_id: Optional[int] = None,
        department_name: Optional[str] = None,
        manager_id: Optional[int] = None,
        limit: Optional[int] = None
):
    stmt = select(Departments)

    if department_id is not None:
        stmt = stmt.where(Departments.id == department_id)
    if department_name is not None:
        stmt = stmt.where(Departments.name == department_name)
    if manager_id is not None:
        stmt = stmt.where(Departments.manager_id == manager_id)
    if limit is not None:
        stmt = stmt.limit(limit)

    return db.execute(stmt).scalars().unique().all()

def update_department(db: Session, department_id: int, department_data: dict):
    department = get_department_by_id(db, department_id)

    if department is None:
        return None

    for key, value in department_data.items():
        setattr(department, key, value)

    db.commit()
    db.refresh(department)

    return department

def delete_department(db: Session, department_id: int):
    department = get_department_by_id(db, department_id)
    if department is None:
        return None
    db.delete(department)
    db.commit()
    return department
