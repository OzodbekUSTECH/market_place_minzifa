from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from config import settings
from sqlalchemy.ext.hybrid import hybrid_property
    
class Type(BaseTable):
    __tablename__ = 'types'
    
    filename: Mapped[str | None]
    name: Mapped[dict] = mapped_column(JSONB)
    description: Mapped[dict | None] = mapped_column(JSONB)
    meta_description: Mapped[dict | None] = mapped_column(JSONB)


    @hybrid_property
    def photo_url(self) -> str | None:
        return f"{settings.TYPES_MEDIA_URL}{self.filename}"


