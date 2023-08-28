from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

    
class TourCommentPhoto(Base):
    __tablename__ = 'tour_comments_photos'
    
    id = Column(Integer, primary_key=True)
    tour_comment_id = Column(Integer, ForeignKey('tour_comments.id'), nullable=False)
    photo_url = Column(String, nullable=False)   
    