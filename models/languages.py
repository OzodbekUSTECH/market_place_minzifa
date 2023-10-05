from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

class Language(BaseTable):
    __tablename__ = 'languages'

    name: Mapped[dict] = mapped_column(type_=JSONB)

    
    
   