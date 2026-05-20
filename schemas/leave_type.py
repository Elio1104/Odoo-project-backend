from typing import Optional

from pydantic import BaseModel, Field


class LeaveTypeCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    default_days_year: float = Field(..., gt=0)


class LeaveTypeRead(BaseModel):
    id: int
    name: str
    default_days_year: float

    model_config = {"from_attributes": True}


class LeaveTypeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    default_days_year: Optional[float] = Field(None, gt=0)

