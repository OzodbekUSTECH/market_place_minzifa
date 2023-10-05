from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

    
class BlogCountry(BaseTable):
    __tablename__ = 'blog_countries'
    
    blog_id: Mapped[int] = mapped_column(ForeignKey("blogs.id", ondelete='CASCADE'))
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    

    