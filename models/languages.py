from models import BaseTable
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, DateTime, JSON
from datetime import datetime
from schemas.languages import LanguageSchema
from utils.locale_handler import LocaleHandler
from sqlalchemy.dialects.postgresql import JSONB

class Language(BaseTable):
    __tablename__ = 'languages'

    name = Column(JSONB, nullable=True)

    async def to_read_model(self, locale: LocaleHandler):
        name = await self._get_trans_columns_by_locale(self.name, locale)
        return LanguageSchema(
            id = self.id,
            name=name,
        )
    
    
   