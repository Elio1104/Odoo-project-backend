from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class RoleEnum(str, Enum):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'
    MANAGER = 'manager'

class EmployeeCreate(BaseModel):
    ## -- User Data -- ##
    email: EmailStr
    role: RoleEnum = RoleEnum.EMPLOYEE

    ## -- Employee Data -- ##
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    position: Optional[str] = Field(None, max_length=100)
    hire_date: date
    department_id: Optional[int] = None

    ## -- Validator -- ##
    @field_validator("first_name", "last_name", mode="before")
    @classmethod
    def strip_and_capitalize(cls, v: str):
        return v.strip().capitalize()

    @model_validator(mode="after")
    def hire_date_not_future(self) -> "EmployeeCreate":
        if self.hire_date > date.today():
            raise ValueError("La date d'embauche ne peut pas être dans le futur")
        return self

class EmployeeRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    position: Optional[str]
    hire_date: date
    department_id: Optional[int]
    email: str
    role: str

    model_config = {"from_attributes": True}

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, min_length=1, max_length=100)
    position: Optional[str] = Field(None, max_length=100)
    department_id: Optional[int] = None
    is_active: Optional[bool] = None
