from models import BaseTable
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import User

class Role(BaseTable):
    __tablename__ = 'roles'

    name: Mapped[dict] = mapped_column(type_=JSONB)

    users: Mapped[list["User"]] = relationship(back_populates="role", lazy="subquery", order_by="User.id")



