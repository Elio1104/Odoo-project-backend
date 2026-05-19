from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum

from models.mixins import TimestampMixin


class Role(str, Enum):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'
    MANAGER = 'manager'

class Users(Base, TimestampMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        nullable=False,
        default=Role.EMPLOYEE
    )

    is_active: Mapped[bool] = mapped_column(
        nullable=False,
        default=True
    )