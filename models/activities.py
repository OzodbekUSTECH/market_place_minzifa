from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from schemas.activities import ActivitySchema
from utils.locale_handler import LocaleHandler
from sqlalchemy.dialects.postgresql import JSONB
    
class Activity(BaseTable):
    __tablename__ = 'activities'
    
    name = Column(JSONB, nullable=False)
    
    async def to_read_model(self, locale: LocaleHandler) -> ActivitySchema:
        name = await self._get_trans_columns_by_locale(self.name, locale)
        return ActivitySchema(
            id=self.id,
            name=name,
        )
