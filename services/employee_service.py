import secrets

from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import Employees
from repositories import user_repo, employee_repo
from schemas.employee import EmployeeCreate, EmployeeUpdate


def create_employee(db: Session, data: EmployeeCreate) -> Employees :
    if user_repo.get_user_by_email(db, data.email):
        raise HTTPException(400, "Email déjà utilisé")

    temp_password = secrets.token_urlsafe(12)

    user = user_repo.create_user(db, {
        'email': data.email,
        'hashed_password': temp_password,
        'role': data.role.value
    })

    employee = employee_repo.create_employee(db, {
        'user_id': user.id,
        'first_name': data.first_name,
        'last_name': data.last_name,
        'position': data.position,
        'hire_date': data.hire_date,
        'department_id': data.department_id
    })

    ##need hash

    return employee

def search(db : Session, **filters):
    return employee_repo.search_employees(db, **filters)

def update_employee(db: Session, employee_id: int, data: EmployeeUpdate):
    payload = data.model_dump(exclude_none=True)
    employee = employee_repo.update_employee(db, employee_id, payload)
    if employee is None:
        raise HTTPException(404, "Employé non trouvé")
    return employee

def delete_employee(db: Session, employee_id: int):
    employee = employee_repo.delete_employee(db, employee_id)
    if employee is None:
        raise HTTPException(404, "Employé non trouvé")
    return employee