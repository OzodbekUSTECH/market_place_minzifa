from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB

class Category(BaseTable):
    __tablename__ = 'categories'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)
    

