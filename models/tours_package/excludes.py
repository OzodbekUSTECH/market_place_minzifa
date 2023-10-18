from models import BaseTable, TourMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import JSONB

class ExcludeInPrice(TourMixin, BaseTable):
    __tablename__ = 'excludes_in_price'

    name: Mapped[dict] = mapped_column(JSONB)
    