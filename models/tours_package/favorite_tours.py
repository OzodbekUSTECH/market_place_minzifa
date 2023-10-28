from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import JSONB
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import Tour

class FavoriteTour(TourMixin, BaseTable):
    __tablename__ = 'favorite_tours'

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    tour: Mapped["Tour"] = relationship(lazy="subquery")
    #title type price country
    