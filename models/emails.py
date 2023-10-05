from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column

class Email(BaseTable):
    __tablename__ = 'emails'

    name: Mapped[str | None]
    email: Mapped[str]
    language: Mapped[str] = mapped_column(index=True)
    