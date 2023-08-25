from database.db import Base
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, DateTime
from schemas.maillist import MailListSchema
from datetime import datetime
class MailList(Base):
    __tablename__ = 'mailing_list'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String)
    created_at = Column(
        DateTime(timezone=True), default=datetime.now
    )
    updated_at = Column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
    def to_read_model(self):
        return MailListSchema(
            **self.__dict__
        )