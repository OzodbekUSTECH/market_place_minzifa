from database.db import Base
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, ForeignKey, DateTime
from datetime import datetime
from utils.locale_handler import LocaleHandler

class BaseTable(Base):
    __abstract__ = True  # Make this class abstract, so it won't create its own table

    id = Column(Integer, primary_key=True, index=True)
    
    created_at = Column(
        DateTime(timezone=True), default=datetime.now
    )
    updated_at = Column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
    
    
    async def _get_trans_columns_by_locale(self, field: dict, locale: LocaleHandler):
        if locale.get_language != "all":
            value = field.get(locale.get_language, "")
            return value
        return field

