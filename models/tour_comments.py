from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

    
class TourComment(BaseTable):
    __tablename__ = 'tour_comments'
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tour_id = Column(Integer, ForeignKey('tours.id'), nullable=False)
    title = Column(String, nullable=False)
    comment_text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False, default=1)
    media = relationship('TourCommentMedia', cascade='all, delete-orphan', lazy='subquery')

   
