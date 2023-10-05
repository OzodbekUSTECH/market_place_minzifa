from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
    
class Country(BaseTable):
    __tablename__ = 'countries'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)
    

