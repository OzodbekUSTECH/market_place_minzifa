from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import (
        User,
        Tour
    )

class Order(TourMixin, BaseTable):
    __tablename__ = "orders"

    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str | None]
    email: Mapped[str | None]
    phone_number: Mapped[str | None]
    start_date: Mapped[str | None]
    end_date: Mapped[str | None]
    amount_of_participants: Mapped[int]
    is_private_request: Mapped[bool]
    wishes: Mapped[str | None] = mapped_column(Text)

    user: Mapped["User"] = relationship(lazy="subquery")
    tour: Mapped["Tour"] = relationship(lazy="subquery")


