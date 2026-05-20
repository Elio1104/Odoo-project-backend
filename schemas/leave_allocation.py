from typing import Optional

from pydantic import BaseModel, Field

from schemas.leave_type import LeaveTypeRead


class LeaveAllocationCreate(BaseModel):
    employee_id: int
    leave_type_id: int
    year: int = Field(..., ge=2000, le=2100)
    total_days: float = Field(..., gt=0)

class LeaveAllocationRead(BaseModel):
    id: int
    employee_id: int
    leave_type_id: int
    year: int
    total_days:float
    used_days:float
    remaining_days:float
    leave_type: LeaveTypeRead

    model_config = {"from_attributes": True}

class LeaveAllocationUpdate(BaseModel):
    total_days: Optional[float] = Field(None, gt=0)
