from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base
from models.mixins import TimestampMixin

if TYPE_CHECKING:
    from models.user import Users, Role

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

    firstName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    lastName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    department_id: Mapped[int] = mapped_column(
        ForeignKey('departments.id'),
    )

    position: Mapped[str] = mapped_column(
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