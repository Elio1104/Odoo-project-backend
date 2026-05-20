from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, SmallInteger, Numeric
from sqlalchemy.orm import mapped_column, Mapped, relationship

from core.database import Base
from models.mixins import TimestampMixin

if TYPE_CHECKING:
    from models.employee import Employees
    from models.leave_type import LeaveTypes


class LeaveAllocations(Base, TimestampMixin):
    __tablename__ = 'leave_allocations'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey('employees.id', ondelete='CASCADE'),
        nullable=False
    )

    leave_type_id: Mapped[int] = mapped_column(
        ForeignKey('leave_types.id'),
        nullable=False
    )

    year: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )

    total_days: Mapped[float] = mapped_column(
        Numeric(5,1),
        nullable=False
    )

    used_days: Mapped[float] = mapped_column(
        Numeric(5,1),
        nullable=False,
        default=0
    )

    employee: Mapped["Employees"] = relationship(
        "Employees",
        back_populates="leave_allocations"
    )

    leave_type: Mapped["LeaveTypes"] = relationship(
        "LeaveTypes",
        back_populates="allocations"
    )

    @property
    def remaining_days(self) -> float:
        return float(self.total_days) - float(self.used_days)
