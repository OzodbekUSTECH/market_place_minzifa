from models import BaseTable
from sqlalchemy import String, Boolean, BigInteger, Column, Integer, Enum, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class TourLanguage(BaseTable):
    __tablename__ = 'tour_languages'

    tour_id = Column(Integer, ForeignKey("tours.id"), nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)

    
    
   