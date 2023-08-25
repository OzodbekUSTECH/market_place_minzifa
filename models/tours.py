from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from schemas.tours import TourSchema, TourPriceSchema

class Tour(Base):
    __tablename__ = 'tours'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    prices = relationship("TourPrice", back_populates="tour", lazy="subquery")
    

    def to_read_model_with_prices(self):
        prices = []
        for price in self.prices:
            prices.append(
                TourPriceSchema(
                    **price.__dict__
                )
            )
        return TourSchema(
            **self.__dict__,
            prices=prices
        )
class TourPrice(Base):
    __tablename__ = 'tour_prices'
    
    id = Column(Integer, primary_key=True)
    tour_id = Column(Integer, ForeignKey('tours.id'))
    currency_id = Column(Integer, ForeignKey('currencies.id'))
    price = Column(Float, nullable=False)
    
    tour = relationship("Tour", back_populates="prices", lazy="subquery")
    currency = relationship("Currency", lazy="subquery")
