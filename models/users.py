from database.db import Base
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from schemas.users import UserSchema
from datetime import datetime
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String)
    company_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    is_traveler_expert = Column(Boolean, default=False)
    is_traveler = Column(Boolean, default=False)    
    created_at = Column(
        DateTime(timezone=True), default=datetime.now
    )
    updated_at = Column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", lazy="subquery")
    favorite_tours = relationship("FavoriteTours", lazy="subquery")
    
    def to_read_model(self):
        return UserSchema(
            **self.__dict__
        )
