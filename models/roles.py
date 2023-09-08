from models import BaseTable
from enum import Enum as PyEnum
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, JSON, ForeignKey
from sqlalchemy.orm import relationship
from schemas.roles import RoleSchema
from utils.locale_handler import LocaleHandler
from sqlalchemy.dialects.postgresql import JSONB

class Role(BaseTable):
    __tablename__ = 'roles'

    name = Column(JSONB, nullable=False)

    role_permissions = relationship("RolePermission", back_populates="role", lazy="subquery")


    async def to_read_model(self, locale: LocaleHandler):
        name = await self._get_trans_columns_by_locale(self.name, locale)
        return RoleSchema(
            id=self.id,
            name=name,
        )



