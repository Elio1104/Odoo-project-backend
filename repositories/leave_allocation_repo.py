from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from models import LeaveAllocations


def create(db: Session, data: dict) -> LeaveAllocations:
    allocation = LeaveAllocations(**data)
    db.add(allocation)
    db.commit()
    db.refresh(allocation)
    return allocation

def get_by_id(db: Session, leave_allocation_id: int) -> Optional[LeaveAllocations]:
    stmt = (
        select(LeaveAllocations)
        .where(LeaveAllocations.id == leave_allocation_id)
        .options(joinedload(LeaveAllocations.leave_type))
    )
    return db.execute(stmt).scalars().one_or_none()

def get_by_employee(db: Session, employee_id: int, year: Optional[int] = None) -> list[LeaveAllocations]:
    stmt = (
        select(LeaveAllocations)
        .where(LeaveAllocations.employee_id == employee_id)
        .options(joinedload(LeaveAllocations.leave_type))
    )
    if year:
        stmt = stmt.where(LeaveAllocations.year == year)
    return db.execute(stmt).scalars().unique().all()

def get_existing(db: Session, employee_id: int, leave_type_id: int, year: int) -> Optional[LeaveAllocations]:
    stmt = select(LeaveAllocations).where(
        LeaveAllocations.employee_id == employee_id,
        LeaveAllocations.leave_type_id == leave_type_id,
        LeaveAllocations.year == year,
    )
    return db.execute(stmt).scalars().one_or_none()

def update(db: Session, leave_allocation_id: int, data: dict) -> Optional[LeaveAllocations]:
    allocation = get_by_id(db, leave_allocation_id)
    if allocation is None:
        return None
    for key, value in data.items():
        setattr(allocation, key, value)
    db.commit()
    db.refresh(allocation)
    return allocation