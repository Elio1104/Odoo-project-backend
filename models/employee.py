from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base
from models.mixins import TimestampMixin

if TYPE_CHECKING:
    from models.user import Users
    from models.department import Departments


class Employees(Base, TimestampMixin):
    __tablename__ = 'employees'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        unique=True,
        nullable=False
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    department_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('departments.id'),
    )

    position: Mapped[Optional[str]] = mapped_column(
        String(100)
    )

    hire_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        nullable=False,
        default=True
    )

    user: Mapped["Users"] = relationship(
        "Users",
        foreign_keys=[user_id],
        back_populates="employee"
    )

    department: Mapped["Departments"] = relationship(
        "Departments",
        foreign_keys=[department_id],
        back_populates="employees"
    )