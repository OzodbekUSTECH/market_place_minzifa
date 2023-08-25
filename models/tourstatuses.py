from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

    
class TourStatus(Base):
    __tablename__ = 'tour_statuses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    tours = relationship("Tour", back_populates="status", lazy="subquery")
