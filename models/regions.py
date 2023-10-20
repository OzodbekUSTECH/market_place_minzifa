from models import BaseTable
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
    
class Region(BaseTable):
    __tablename__ = 'regions'
    
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    name: Mapped[dict] = mapped_column(JSONB)
    description: Mapped[dict | None] = mapped_column(JSONB)
    meta_description: Mapped[dict | None] = mapped_column(JSONB)
    

