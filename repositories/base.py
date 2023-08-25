from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from fastapi import Query

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
     