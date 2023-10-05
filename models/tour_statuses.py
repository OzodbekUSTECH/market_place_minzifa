from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
 

    
class TourStatus(BaseTable):
    __tablename__ = 'tour_statuses'
    
    name: Mapped[dict] = mapped_column(type_=JSONB)

