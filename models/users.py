from models import BaseTable
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from schemas.users import UserSchema
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property

class User(BaseTable):
    __tablename__ = 'users'

    email = Column(String, index=True)
    password = Column(String)
    company_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)  
    role_id = Column(Integer, ForeignKey("roles.id"))
    link = Column(String, nullable=True)
    about = Column(Text, nullable=True)

    role = relationship("Role", lazy="subquery")
    favorite_tours = relationship("FavoriteTours", cascade="all, delete-orphan", lazy="subquery")
    tours = relationship("Tour", back_populates="user",cascade="all, delete-orphan", lazy="subquery")
    
    travelers = relationship(
        "TravelersAndManagersAssociation",
        primaryjoin="User.id == TravelersAndManagersAssociation.manager_id",
        # back_populates="traveler",
        # cascade="all, delete-orphan",
        lazy="subquery"
    )
    
    managers = relationship(
        "TravelersAndManagersAssociation",
        primaryjoin="User.id == TravelersAndManagersAssociation.traveler_id",
        # back_populates="manager",
        # cascade="all, delete-orphan",
        lazy="subquery"
    )
    @hybrid_property
    def rating(self):
        
        if self.tours:
            all_ratings = []
            
            for tour in self.tours:
                for comment in tour.tour_comments:
                    all_ratings.append(comment.rating)
                    
            if all_ratings:
                return sum(all_ratings) / len(all_ratings)
        return 1
    
