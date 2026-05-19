from sqlalchemy import select
from sqlalchemy.orm import Session

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

def read_employee(db: Session, employee_id: int):
    stmt = select(Employees).where(Employees.id == employee_id)
    result = db.execute(stmt).scalars().one_or_none()

    return result

