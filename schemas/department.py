from typing import Optional

from pydantic import BaseModel, Field


class DepartmentCreate(BaseModel):
    ## -- Department Data -- ##
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    manager_id: Optional[int] = None

class DepartmentRead(BaseModel):
    id: int
    name: str
    description: Optional[str]
    manager_id: Optional[int]

class DepartmentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    manager_id: Optional[int] = None
