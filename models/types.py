from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

    
class Type(BaseTable):
    __tablename__ = 'types'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)
    

