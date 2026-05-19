from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from models import Users
from models.employee import Employees


def create_employee(db: Session, employee_data: dict):
    employee = Employees(
        user_id=employee_data['user_id'],
        first_name=employee_data['first_name'],
        last_name=employee_data['last_name'],
        position=employee_data['position'],
        hire_date=employee_data['hire_date'],
        department_id=employee_data['department_id']
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee

def get_employee_by_id(db: Session, employee_id: int):
    stmt = select(Employees).where(Employees.id == employee_id)
    result = db.execute(stmt).scalars().one_or_none()

    return result

def search_employees(
    db: Session,
    employee_id: Optional[int] = None,
    email: Optional[str] = None,
    department_id: Optional[int] = None,
    role: Optional[str] = None,
    is_active: Optional[bool] = None,
    limit: Optional[int] = None
) -> list[Employees]:
    stmt = (
        select(Employees)
        .join(Employees.user)
        .options(joinedload(Employees.user))
    )

    if employee_id is not None:
        stmt = stmt.where(Employees.id == employee_id)
    if email is not None:
        stmt = stmt.where(Users.email == email)
    if department_id is not None:
        stmt = stmt.where(Employees.department_id == department_id)
    if role is not None:
        stmt = stmt.where(Users.role == role)
    if is_active is not None:
        stmt = stmt.where(Employees.is_active == is_active)
    if limit is not None:
        stmt = stmt.limit(limit)

    return db.execute(stmt).scalars().unique().all()

