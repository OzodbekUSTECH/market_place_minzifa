from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from fastapi import Query
from datetime import date
from fuzzywuzzy import fuzz, process

class Pagination:
    def __init__(self, page: int = Query(1, ge=1), page_size: int = Query(100, le=100)):
        self.page = page
        self.page_size = page_size
    
    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size
        
    @property
    def limit(self) -> int:
        return self.page_size



    def filter_tour(self, tour):
        if self.status_id and tour.status_id != self.status_id:
            return False

        if self.query and fuzz.partial_ratio(self.query.lower(), tour.title.lower()) <= 60:
            return False

        if self.tour_rating and (tour.user.rating < self.tour_rating or tour.user.rating >= self.tour_rating + 0.5):
            return False

        if self.start_date and tour.start_date != self.start_date:
            return False

        if self.end_date and tour.end_date != self.end_date:
            return False

        if self.country and tour.country != self.country:
            return False

        if self.region and tour.region != self.region:
            return False

        if self.currency_id is not None and self.price is not None:
            for tour_price in tour.prices:
                if tour_price.currency_id == self.currency_id and tour_price.price >= self.price:
                    return True
            return False

        return True
    
class BaseRepository:
    def __init__(self, session: Session, model:DeclarativeMeta):
        self.session = session
        self.model = model

    async def create(self, data: dict):
        instance = self.model(**data)  # Создаем экземпляр модели с переданными данными
        self.session.add(instance)
        self.session.commit()
        return instance
    
    async def get_by_id(self, id: int):
        instance = self.session.query(self.model).filter(self.model.id == id).first()
        self.session.commit()
        return instance
    
    async def get_by_email(self, email: str):
        instance = self.session.query(self.model).filter(self.model.email == email).first()
        self.session.commit()
        return instance
    
    async def get_all(self, pagination: Pagination = None):
        query = self.session.query(self.model).order_by(self.model.id)
    
        if pagination:
            instances = query.offset(pagination.offset).limit(pagination.limit).all()
        else:
            instances = query.all()
        self.session.commit()
        
        return instances


    
    async def update(self, id: int, data: dict):
        instance = self.session.query(self.model).filter(self.model.id == id).one()

        for field, value in data.items():
            setattr(instance, field, value)
        self.session.commit()
        return instance
    
    async def delete(self, id: int):
        instance = self.session.query(self.model).filter(self.model.id == id).first()
        self.session.delete(instance)
        self.session.commit()
        return instance
     