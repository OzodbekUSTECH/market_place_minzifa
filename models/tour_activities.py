from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

    
class TourActivity(BaseTable):
    __tablename__ = 'tour_activities'
    
    tour_id = Column(Integer, ForeignKey('tours.id'))
    activity_id = Column(Integer, ForeignKey('activities.id'))

    tour = relationship("Tour", back_populates="activities", lazy="subquery")
    activity = relationship("Activity", lazy="subquery")
