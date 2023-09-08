from models import BaseTable
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from schemas.travelermanagers import TravelersSchema, ManagersSchema, AssociationTravelAndManagerSchema


class TravelersAndManagersAssociation(BaseTable):
    __tablename__ = 'travelers_managers'

    traveler_id = Column(Integer, ForeignKey("users.id"), index=True)
    manager_id = Column(Integer, ForeignKey("users.id"), index=True)

    