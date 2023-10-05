from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class TourLanguage(TourMixin, BaseTable):
    __tablename__ = 'tour_languages'

    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"))

   
    
    
   