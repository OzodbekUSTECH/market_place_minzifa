from models import BaseTable
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB
from config import settings
from sqlalchemy.ext.hybrid import hybrid_property

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import Country


class Blog(BaseTable):
    __tablename__ = 'blogs'
    
    title: Mapped[dict] = mapped_column(type_=JSONB)
    meta_description: Mapped[dict] = mapped_column(type_=JSONB)
    description: Mapped[dict] = mapped_column(type_=JSONB)
    views: Mapped[int] = mapped_column(default=0, server_default="0")

    @hybrid_property
    def country_ids(self):
        return [country.id for country in self.countries]

    media: Mapped[list["BlogMedia"]] = relationship(lazy="subquery", cascade="all, delete-orphan")
    countries: Mapped[list["Country"]] = relationship(secondary="blog_countries",lazy="subquery", cascade="all, delete")

    async def increase_view_count(self):
        self.views += 1


class BlogMedia(BaseTable):
    __tablename__ = "blog_media_group"

    blog_id: Mapped[int] = mapped_column(ForeignKey("blogs.id", ondelete='CASCADE'))
    filename: Mapped[str]

    @hybrid_property
    def media_url(self) -> str | None:
        if self.filename:
            return f"{settings.BLOG_MEDIA_URL}{self.filename}"
        return None

    