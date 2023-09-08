from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date, ARRAY, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from utils.locale_handler import LocaleHandler
from schemas.tours import TourSchema
class Tour(BaseTable):
    __tablename__ = 'tours'
    
    title = Column(JSON, nullable=False)
    description = Column(JSON, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status_id = Column(Integer, ForeignKey('tour_statuses.id'), nullable=False, index=True)
    prices = relationship("TourPrice", cascade="all, delete-orphan", lazy="subquery")
    status = relationship("TourStatus", back_populates="tours", lazy="subquery")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    country = Column(JSON, nullable=False)
    region = Column(JSON, nullable=False)
    total_places = Column(Integer, nullable=False)
    free_places = Column(Integer, nullable=False)
    age_group = Column(String, nullable=False)
    children_age = Column(String, nullable=False)
    level_of_activity = Column(JSON, nullable=False)
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
    
    
    async def to_read_model(self, locale: LocaleHandler):
        title = await self._get_trans_columns_by_locale(self.title, locale)
        description = await self._get_trans_columns_by_locale(self.description, locale)
        country = await self._get_trans_columns_by_locale(self.country, locale)
        region = await self._get_trans_columns_by_locale(self.region, locale)
        level_of_activity = await self._get_trans_columns_by_locale(self.level_of_activity, locale)
        return TourSchema(
            id=self.id,
            title=title,
            description=description,
            user_id=self.user_id,
            status_id=self.status_id,
            start_date=self.start_date,
            end_date=self.end_date,
            country=country,
            region=region,
            total_places=self.total_places,
            free_places=self.free_places,
            age_group=self.age_group,
            children_age=self.children_age,
            level_of_activity=level_of_activity,
            amount_views=self.amount_views,
            amount_comments=self.amount_comments,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


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

    

   