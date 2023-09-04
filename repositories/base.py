from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from fastapi import Query
from datetime import date
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

class FilterTours:
    def __init__(
            self,
            query: str = Query(None),
            status_id: int = Query(None),
            tour_rating: float = Query(None, le=5.0, ge=0.0),
            start_date: date = Query(None),
            end_date: date = Query(None),
            country: str = Query(None),
            region: str = Query(None),
            currency_id: int = Query(None),
            price: int = Query(None),
    ):
        self.query = query
        self.status_id = status_id
        self.tour_rating = tour_rating
        self.start_date = start_date
        self.end_date = end_date
        self.country = country
        self.region = region
        self.currency_id = currency_id
        self.price = price

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
     