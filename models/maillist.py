from database.db import Base
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum


class MailList(Base):
    __tablename__ = 'mailing_list'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String)