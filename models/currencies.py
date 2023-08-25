from database.db import Base
from sqlalchemy import Column, Integer, String, Float


class Currency(Base):
    __tablename__ = 'currencies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    exchange_rate = Column(Float, nullable=False)
