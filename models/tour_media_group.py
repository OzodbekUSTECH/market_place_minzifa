from models import BaseTable, TourMixin
from sqlalchemy.orm import Mapped
from sqlalchemy.ext.hybrid import hybrid_property
from config import settings

class TourMedia(TourMixin, BaseTable):
    __tablename__ = 'tour_media_group'

    filename: Mapped[str]

    @hybrid_property
    def media_url(self):
        return f"{settings.TOURS_MEDIA_URL}{self.filename}"

   
    
    
   