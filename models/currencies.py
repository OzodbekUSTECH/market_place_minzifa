from models import BaseTable
from sqlalchemy import Column, Integer, String, Float


class Currency(BaseTable):
    __tablename__ = 'currencies'
    
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    exchange_rate = Column(Float, nullable=False)
