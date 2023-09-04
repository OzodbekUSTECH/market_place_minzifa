from models import BaseTable
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, JSON, ForeignKey
from sqlalchemy.orm import relationship
from schemas.rolepermissions import RolePermissionsSchema

class RolePermission(BaseTable):
    __tablename__ = 'role_permissions'

    role_id = Column(Integer, ForeignKey('roles.id'), index=True)
    permission_id = Column(Integer, ForeignKey('permissions.id'), index=True)

    role = relationship("Role", back_populates="role_permissions", lazy="subquery")
    permission = relationship("Permission", back_populates="role_permissions", lazy="subquery")

    def to_read_model(self):
        return RolePermissionsSchema(
            **self.__dict__
        )
    
    