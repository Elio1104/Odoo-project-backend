from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum, DateTime, func
from datetime import datetime

class Role(str, Enum):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'
    MANAGER = 'manager'

class User(Base):
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

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )