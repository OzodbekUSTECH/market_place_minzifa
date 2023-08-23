from database.db import Base
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from schemas.travelermanagers import TravelersSchema, ManagersSchema, AssociationTravelAndManagerSchema


class TravelersAndManagersAssociation(Base):
    __tablename__ = 'travelers_managers'

    id = Column(Integer, primary_key=True, index=True)
    traveler_id = Column(Integer, ForeignKey("users.id"), index=True)
    manager_id = Column(Integer, ForeignKey("users.id"), index=True)

    traveler = relationship("User", foreign_keys=[traveler_id], lazy="subquery")
    manager = relationship("User", foreign_keys=[manager_id], lazy="subquery")    
    
    def to_read_model(self):
        return AssociationTravelAndManagerSchema(
            **self.__dict__
        )
    
    def to_read_model_of_traveler(self):
        return TravelersSchema(
            **self.traveler.__dict__  
        )
    
    def to_read_model_of_manager(self):
        return ManagersSchema(
            **self.manager.__dict__  
        )