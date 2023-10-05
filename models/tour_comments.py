from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import TYPE_CHECKING
from sqlalchemy.ext.hybrid import hybrid_property
from config import settings
if TYPE_CHECKING:
    from models import (
        User,
        Tour,
    )
    
class TourComment(TourMixin, BaseTable):
    __tablename__ = 'tour_comments'

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment_text: Mapped[str]
    rating: Mapped[float | None]
    
    parent_comment_id: Mapped[int | None] = mapped_column(ForeignKey("tour_comments.id"))

    user: Mapped["User"] = relationship(lazy="subquery")
    tour: Mapped["Tour"] = relationship(lazy="subquery")

    media: Mapped[list["TourCommentMedia"]] = relationship(cascade="all, delete-orphan", lazy="subquery")
    replies: Mapped[list["TourComment"]] = relationship(cascade="all, delete-orphan", lazy="immediate")




class TourCommentMedia(BaseTable):
    __tablename__ = 'tour_comments_media'
    
    comment_id: Mapped[int] = mapped_column(ForeignKey("tour_comments.id", ondelete="CASCADE"))
    filename: Mapped[str]
    
    @hybrid_property
    def media_url(self):
        return f"{settings.TOUR_COMMENTS_MEDIA_URL}{self.filename}"

   
    
    
   
