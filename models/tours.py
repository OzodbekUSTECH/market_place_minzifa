from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property

class Tour(BaseTable):
    __tablename__ = 'tours'
    
    title = Column(String, nullable=False)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status_id = Column(Integer, ForeignKey('tour_statuses.id'), nullable=False, index=True)
    prices = relationship("TourPrice", back_populates="tour", lazy="subquery")
    status = relationship("TourStatus", back_populates="tours", lazy="subquery")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    country = Column(String, nullable=False)
    region = Column(String, nullable=False)
    activities = relationship("TourActivity", back_populates="tour", lazy="subquery")
    tour_comments = relationship("TourComment", lazy="subquery")
    user = relationship("User", back_populates="tours", lazy="subquery")


    
    @hybrid_property
    def amount_comments(self):
        return len(self.tour_comments)