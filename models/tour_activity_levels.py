from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

    
class TourActivityLevel(BaseTable):
    __tablename__ = 'tour_activity_levels'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)
    level_number: Mapped[int]    

    