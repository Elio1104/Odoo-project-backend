from sqlalchemy.orm import Session

from models.employee import Employees


def create_employee(db: Session, employee_data: dict):
    employee = Employees(
        user_id=employee_data['user_id'],
        firstName=employee_data['first_name'],
        lastName=employee_data['last_name'],
        position=employee_data['position'],
        hire_date=employee_data['hire_date'],
        department_id=employee_data['department_id']
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee
