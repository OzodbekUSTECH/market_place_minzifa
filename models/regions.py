from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
    
class Region(BaseTable):
    __tablename__ = 'regions'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)
    

