from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

    
class TourCountry(TourMixin, BaseTable):
    __tablename__ = 'tour_countries'
    
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    

    