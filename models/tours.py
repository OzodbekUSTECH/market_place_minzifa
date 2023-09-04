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
    total_places = Column(Integer, nullable=False)
    free_places = Column(Integer, nullable=False)
    # view_count = Column(Integer, default=0)  # Добавляем поле для счетчика просмотров
    views = relationship("IPTourView", lazy="subquery")
    activities = relationship("TourActivity", back_populates="tour", lazy="subquery")
    tour_comments = relationship("TourComment", lazy="subquery")
    user = relationship("User", back_populates="tours", lazy="subquery")
    
    
    @hybrid_property
    def amount_comments(self):
        return len(self.tour_comments)
    
    @hybrid_property
    def amount_views(self):
        return len(self.views)
    # def increment_view_count(self):
    #     self.view_count += 1


class IPTourView(BaseTable):
    __tablename__ = 'ip_tour_views'

    ip_address = Column(String, nullable=False)
    tour_id = Column(Integer, ForeignKey('tours.id'), nullable=False)  

    
    

   