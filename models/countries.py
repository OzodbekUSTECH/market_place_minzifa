from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from config import settings
class Country(BaseTable):
    __tablename__ = 'countries'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)
    title: Mapped[dict] = mapped_column(type_=JSONB)
    meta_description: Mapped[dict | None] = mapped_column(type_=JSONB)
    description: Mapped[dict | None] = mapped_column(type_=JSONB)
    filename: Mapped[str]

    @property
    def photo_url(self) -> str:
        return f"{settings.COUNTRY_MEDIA_URL}{self.filename}"

