from sqlalchemy.orm import declarative_base, sessionmaker
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
        self.session.add(instance)      # Добавляем экземпляр в сессию
        self.session.commit()
        return instance
    
    async def get_by_id(self, id: int):
        instance = self.session.query(self.model).filter(self.model.id == id).first()
        return instance
    
    async def get_by_email(self, email: str):
        instance = self.session.query(self.model).filter(self.model.email == email).first()
        return instance
    
    async def get_all(self, pagination: Pagination):
        instances = self.session.query(self.model).offset(pagination.offset).limit(pagination.limit).all()
        return instances

    
    async def update(self, id: int, data: dict):
        instance = self.session.query(self.model).filter(self.model.id == id).one()

        for field, value in data.items():
            setattr(instance, field, value)

        self.session.commit()
        self.session.refresh(instance)
        return instance
    
    async def delete(self, id: int):
        instance = self.session.query(self.model).filter(self.model.id == id).first()
        self.session.delete(instance)
        self.session.commit()

        return instance
    

    #just for mails
    