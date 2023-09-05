from models import BaseTable
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, DateTime
from datetime import datetime

class Language(BaseTable):
    __tablename__ = 'languages'

    name = Column(String, nullable=True)
    
    
   