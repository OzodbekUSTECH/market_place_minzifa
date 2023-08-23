from database.db import Base
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from schemas.users import UserSchema

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String)
    company_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    is_traveler_expert = Column(Boolean, default=False)
    is_traveler = Column(Boolean, default=False)    

    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role")
    
    
    def to_read_model(self):
        return UserSchema(
            **self.__dict__
        )
