from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

    
class TourPrice(BaseTable):
    __tablename__ = 'tour_prices'
    
    tour_id = Column(Integer, ForeignKey('tours.id'))
    currency_id = Column(Integer, ForeignKey('currencies.id'))
    price = Column(Integer, nullable=False)
    discount_percentage = Column(Integer, nullable=True)
    new_price = Column(Integer, nullable=True)
    

    tour = relationship("Tour", back_populates="prices", lazy="subquery")
    currency = relationship("Currency", lazy="subquery")
