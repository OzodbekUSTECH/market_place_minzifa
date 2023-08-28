from database.db import Base
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from schemas.users import UserSchema
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property

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
    tours = relationship("Tour", back_populates="user", lazy="subquery")
    travelers = relationship(
        "TravelersAndManagersAssociation",
        primaryjoin="User.id == TravelersAndManagersAssociation.traveler_id",
        back_populates="traveler",
        lazy="subquery"
    )
    
    managers = relationship(
        "TravelersAndManagersAssociation",
        primaryjoin="User.id == TravelersAndManagersAssociation.manager_id",
        back_populates="manager",
        lazy="subquery"
    )
    @hybrid_property
    def rating(self):
        all_ratings = []
        
        for tour in self.tours:
            for comment in tour.tour_comments:
                all_ratings.append(comment.rating)
                
        if all_ratings:
            return sum(all_ratings) / len(all_ratings)
        return 1
    
