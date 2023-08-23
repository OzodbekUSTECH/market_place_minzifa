from database.db import Base
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum
from schemas.maillist import MailListSchema

class MailList(Base):
    __tablename__ = 'mailing_list'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String)

    def to_read_model(self):
        return MailListSchema(
            **self.__dict__
        )