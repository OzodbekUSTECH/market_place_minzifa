from models import BaseTable
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, JSON, ForeignKey
from sqlalchemy.orm import relationship
from schemas.roles import RoleSchema

class Role(BaseTable):
    __tablename__ = 'roles'

    name = Column(String)

    role_permissions = relationship("RolePermission", back_populates="role", lazy="subquery")


    def to_read_model(self):
        return RoleSchema(
            **self.__dict__
        )



