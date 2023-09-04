from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

    
class TourStatus(BaseTable):
    __tablename__ = 'tour_statuses'
    
    name = Column(String, nullable=False)
    
    tours = relationship("Tour", back_populates="status", lazy="subquery")
