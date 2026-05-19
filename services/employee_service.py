import secrets

from sqlalchemy.orm import Session

from repositories import user_repo, employee_repo
from schemas.employee import EmployeeCreate


def create_employee(db: Session, data: EmployeeCreate):
    temp_password = secrets.token_urlsafe(12)

    user = user_repo.create_user(db, {
        'email': data.email,
        'hashed_password': temp_password,
        'role': 'employee'
    })

    employee = employee_repo.create_employee(db, {
        'user_id': user.id,
        'first_name': data.first_name,
        'last_name': data.last_name,
        'position': data.position,
        'hire_date': data.hire_date,
        'department_id': data.department_id
    })

    print(temp_password) ##del

    return employee