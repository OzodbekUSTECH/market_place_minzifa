from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Tour(Base):
    __tablename__ = 'tours'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True), default=datetime.now
    )
    updated_at = Column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
    user_id = Column(Integer, ForeignKey("users.id"))
    status_id = Column(Integer, ForeignKey('tour_statuses.id'), nullable=False, index=True)
    prices = relationship("TourPrice", back_populates="tour", lazy="subquery")
    status = relationship("TourStatus", back_populates="tours", lazy="subquery")

    activities = relationship("TourActivity", back_populates="tour", lazy="subquery")
    tour_comments = relationship("TourComment", lazy="subquery")

