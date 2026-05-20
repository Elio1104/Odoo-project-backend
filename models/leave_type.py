from typing import List, TYPE_CHECKING

from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base
from models.mixins import TimestampMixin

if TYPE_CHECKING:
    from models.leave_allocation import LeaveAllocations


class LeaveTypes(Base, TimestampMixin):
    __tablename__ = 'leave_types'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    default_days_year: Mapped[float] = mapped_column(
        Numeric(5,1),
        nullable=False
    )

    allocations: Mapped[List["LeaveAllocations"]] = relationship(
        "LeaveAllocations",
        back_populates="leave_type",
    )

