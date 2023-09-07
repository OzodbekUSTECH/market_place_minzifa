from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property

class Tour(BaseTable):
    __tablename__ = 'tours'
    
    title = Column(String, nullable=False)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status_id = Column(Integer, ForeignKey('tour_statuses.id'), nullable=False, index=True)
    prices = relationship("TourPrice", cascade="all, delete-orphan", lazy="subquery")
    status = relationship("TourStatus", back_populates="tours", lazy="subquery")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    country = Column(String, nullable=False)
    region = Column(String, nullable=False)
    total_places = Column(Integer, nullable=False)
    free_places = Column(Integer, nullable=False)
    age_group = Column(String, nullable=False)
    children_age = Column(String, nullable=False)
    level_of_activity = Column(String, nullable=False)
    languages = relationship("TourLanguage", cascade="all, delete-orphan", lazy="subquery")
    # view_count = Column(Integer, default=0)  # Добавляем поле для счетчика просмотров
    views = relationship("IPAndToursView", cascade="all, delete-orphan", lazy="subquery")
    activities = relationship("TourActivity", back_populates="tour", cascade="all, delete-orphan", lazy="subquery")
    tour_comments = relationship("TourComment", cascade="all, delete-orphan", lazy="subquery")
    user = relationship("User", back_populates="tours", lazy="subquery")
    
    def get_list_of_language_ids(self):
        res = []
        for language in self.languages:
            res.append(language.language_id)
        return res
    @hybrid_property
    def amount_comments(self):
        return len(self.tour_comments)
    
    @hybrid_property
    def amount_views(self):
        amount = 0
        for view in self.views:
            amount += view.visited_times
        return amount
    
    
    # def increment_view_count(self):
    #     self.view_count += 1


class IPTourView(BaseTable):
    __tablename__ = 'ip_tour_views'

    
    ip_address = Column(String, nullable=False)
    viewed_tours = relationship("IPAndToursView", lazy="subquery")
    
    def get_list_of_tour_ids(self):
        tour_ids = []
        for instance in self.viewed_tours:
            tour_ids.append(instance.tour_id)
        return tour_ids
    
class IPAndToursView(BaseTable):
    __tablename__ = 'ip_and_tours_views'

    ip_id = Column(Integer, ForeignKey("ip_tour_views.id"), nullable=False)
    visited_times = Column(Integer, default=0)
    tour_id = Column(Integer, ForeignKey("tours.id"), nullable=False)

    def increase_visited_times(self):
        self.visited_times += 1

    

   