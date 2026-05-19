from typing import TYPE_CHECKING, Optional

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base
from models.mixins import TimestampMixin

if TYPE_CHECKING:
    from models.employee import Employees


class Departments(Base, TimestampMixin):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text()
    )

    manager_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('employees.id', use_alter=True, name='fk_department_manager'),
    )

    employees: Mapped[Optional["Employees"]] = relationship(
        "Employees",
        foreign_keys="[Employees.department_id]",
        back_populates="department"
    )

    manager: Mapped[Optional["Employees"]] = relationship(
        "Employees",
        foreign_keys=[manager_id],
        post_update=True,
    )