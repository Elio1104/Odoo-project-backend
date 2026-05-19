from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base
from models.mixins import TimestampMixin


class Departments(Base, TimestampMixin):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text()
    )

    manager_id: Mapped[int] = mapped_column(
        ForeignKey('employees.id'),
    )