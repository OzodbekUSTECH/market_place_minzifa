from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Tour(Base):
    __tablename__ = 'tours'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    prices = relationship("TourPrice", back_populates="tour", lazy="subquery")



