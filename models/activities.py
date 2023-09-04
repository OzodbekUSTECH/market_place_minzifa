from models import BaseTable
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

    
class Activity(BaseTable):
    __tablename__ = 'activities'
    
    name = Column(String, nullable=False)
    

