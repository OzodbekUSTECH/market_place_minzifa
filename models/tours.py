from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Tour(Base):
    __tablename__ = 'tours'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    prices = relationship("TourPrice", back_populates="tour", lazy="subquery")

class TourPrice(Base):
    __tablename__ = 'tour_prices'
    
    id = Column(Integer, primary_key=True)
    tour_id = Column(Integer, ForeignKey('tours.id'))
    currency_id = Column(Integer, ForeignKey('currencies.id'))
    price = Column(Float, nullable=False)
    
    tour = relationship("Tour", back_populates="prices", lazy="subquery")
    currency = relationship("Currency", lazy="subquery")
