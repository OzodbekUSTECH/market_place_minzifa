from models import BaseTable
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, DateTime
from schemas.maillist import MailListSchema
from datetime import datetime
class MailList(BaseTable):
    __tablename__ = 'mailing_list'

    name = Column(String, nullable=True)
    email = Column(String)
    
    def to_read_model(self):
        return MailListSchema(
            **self.__dict__
        )