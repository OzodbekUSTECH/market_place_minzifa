from database.db import Base
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, JSON, ForeignKey
from sqlalchemy.orm import relationship


class RolePermission(Base):
    __tablename__ = 'role_permissions'

    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True, index=True)
    permission_id = Column(Integer, ForeignKey('permissions.id'), primary_key=True)

    role = relationship("Role", back_populates="role_permissions", lazy="joined")
    permission = relationship("Permission", back_populates="role_permissions", lazy="joined")
