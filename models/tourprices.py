from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

    
class TourPrice(BaseTable):
    __tablename__ = 'tour_prices'
    
    tour_id = Column(Integer, ForeignKey('tours.id'))
    currency_id = Column(Integer, ForeignKey('currencies.id'))
    price = Column(Integer, nullable=False)
    discount_percentage = Column(Float, nullable=True)
    new_price = Column(Float, nullable=True)
    

