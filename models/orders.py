from models import BaseTable
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

class BaseOrder(BaseTable):
    __abstract__ = True

    tour_id: Mapped[int] = mapped_column(ForeignKey("tours.id"))
    name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str]

    participants: Mapped[int] = mapped_column(default=1, server_default="1")