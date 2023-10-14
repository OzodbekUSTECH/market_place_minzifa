from models import BaseTable, TourMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

class TourImportant(TourMixin, BaseTable):
    __tablename__ = 'tour_importants'

    question: Mapped[dict] = mapped_column(JSONB)
    answer: Mapped[dict] = mapped_column(JSONB)