from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

    
class TourCommentMedia(BaseTable):
    __tablename__ = 'tour_comments_media'
    
    tour_comment_id = Column(Integer, ForeignKey('tour_comments.id'), nullable=False)
    media_url = Column(String, nullable=False)   
    