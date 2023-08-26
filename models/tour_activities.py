from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

    
class TourActivity(Base):
    __tablename__ = 'tour_activities'
    
    id = Column(Integer, primary_key=True)
    tour_id = Column(Integer, ForeignKey('tours.id'))
    activity_id = Column(Integer, ForeignKey('activities.id'))

    tour = relationship("Tour", back_populates="activities", lazy="subquery")
    activity = relationship("Activity", lazy="subquery")
