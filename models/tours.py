from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from schemas.tours import TourSchema, TourPriceSchema

from sqlalchemy.orm.attributes import InstrumentedAttribute

class Tour(Base):
    __tablename__ = 'tours'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    prices = relationship("TourPrice", back_populates="tour", lazy="subquery")

    def to_read_model_with_prices(self):
        prices_data = [
            TourPriceSchema(
                **{attr: getattr(price, attr) for attr in price.__class__.__dict__.keys() if isinstance(getattr(price.__class__, attr), InstrumentedAttribute)}
            )
            for price in self.prices
        ]
        
        return TourSchema(
            **{attr: getattr(self, attr) for attr in self.__class__.__dict__.keys() if isinstance(getattr(self.__class__, attr), InstrumentedAttribute)},
            prices=prices_data
        )


    
class TourPrice(Base):
    __tablename__ = 'tour_prices'
    
    id = Column(Integer, primary_key=True)
    tour_id = Column(Integer, ForeignKey('tours.id'))
    currency_id = Column(Integer, ForeignKey('currencies.id'))
    price = Column(Float, nullable=False)
    
    tour = relationship("Tour", back_populates="prices", lazy="subquery")
    currency = relationship("Currency", lazy="subquery")
