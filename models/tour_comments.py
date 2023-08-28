from database.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

    
class TourComment(Base):
    __tablename__ = 'tour_comments'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tour_id = Column(Integer, ForeignKey('tours.id'), nullable=False)
    title = Column(String, nullable=False)
    comment_text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False, default=1)
    photos = relationship('TourCommentMedia', cascade='all, delete-orphan', lazy='subquery')

    created_at = Column(
        DateTime(timezone=True), default=datetime.now
    )
    updated_at = Column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
    
