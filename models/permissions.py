from models import BaseTable
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, JSON, ForeignKey
from sqlalchemy.orm import relationship
from schemas.roles import RolePermissionsSchema

class Permission(BaseTable):
    __tablename__ = 'permissions'

    name = Column(String)
    endpoint = Column(String)
    role_permissions = relationship("RolePermission", back_populates="permission", lazy="subquery")

    @property
    def role_id(self):
        if self.role_permissions:
            return self.role_permissions[0].role_id
        return None
    
    def to_read_model(self):
        return RolePermissionsSchema(
            **self.__dict__,
            role_id=self.role_id,
        )