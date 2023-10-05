from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

    
class TourChildrenAge(BaseTable):
    __tablename__ = 'tour_children_ages'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)
    

