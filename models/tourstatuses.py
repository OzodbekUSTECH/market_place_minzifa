from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from schemas.tourstatuses import TourStatusSchema
from utils.locale_handler import LocaleHandler
from sqlalchemy.dialects.postgresql import JSONB
    
class TourStatus(BaseTable):
    __tablename__ = 'tour_statuses'
    
    name = Column(JSONB, nullable=False)
    
    tours = relationship("Tour", back_populates="status", lazy="subquery")

    async def to_read_model(self, locale: LocaleHandler):
        name = await self._get_trans_columns_by_locale(self.name, locale)
        return TourStatusSchema(
            id=self.id,
            name=name
        )