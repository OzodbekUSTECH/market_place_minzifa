from database.db import Base
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, ForeignKey, DateTime
from datetime import datetime

class BaseTable(Base):
    __abstract__ = True  # Make this class abstract, so it won't create its own table

    id = Column(Integer, primary_key=True, index=True)
    
    created_at = Column(
        DateTime, default=datetime.now
    )
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )
    
    
