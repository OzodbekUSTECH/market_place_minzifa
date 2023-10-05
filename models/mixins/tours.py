from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy import ForeignKey


class TourMixin:


    @declared_attr
    def tour_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("tours.id", ondelete="CASCADE"))
    
    
    
    
