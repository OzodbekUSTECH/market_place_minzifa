from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

    
class Accommodation(BaseTable):
    __tablename__ = 'accommodations'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)
    

