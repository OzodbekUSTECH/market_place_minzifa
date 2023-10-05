from models import BaseTable
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import (
        Role,
        Tour,
    )

class User(BaseTable):
    __tablename__ = 'users'

    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(index=True, unique=True)
    password: Mapped[str]
    company_name: Mapped[str | None]
    phone_number: Mapped[str | None]  
    link: Mapped[str | None]
    about: Mapped[str | None] = mapped_column(Text)
    is_banned: Mapped[bool] = mapped_column(default=False, server_default="false")
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    role: Mapped["Role"] = relationship(back_populates="users", lazy="selectin")

    travel_expert: Mapped["User"] = relationship(
        secondary="user_employees",
        primaryjoin="User.id == UserEmployee.employee_id",
        secondaryjoin="User.id == UserEmployee.user_id",
        lazy="immediate",
        overlaps="employees"  # Add this parameter
    )

    # Отношение к путешественникам (множественное отношение)
    employees: Mapped[list["User"]] = relationship(
        secondary="user_employees",
        primaryjoin="User.id == UserEmployee.user_id",
        secondaryjoin="User.id == UserEmployee.employee_id",
        lazy="immediate",
        overlaps="travel_expert"  # Add this parameter
    )
    tours: Mapped[list["Tour"]] = relationship(back_populates="user", lazy="subquery")
    
    # @hybrid_property
    # def rating(self):
        
    #     if self.tours:
    #         all_ratings = []
            
    #         for tour in self.tours:
    #             for comment in tour.tour_comments:
    #                 if not comment.is_replied:
    #                     all_ratings.append(comment.rating)
    #         if all_ratings:
    #             return sum(all_ratings) / len(all_ratings)
    #     return 1
    
    
    # role: Mapped["Role"] = relationship(back_populates="users", lazy="subquery")
    # favorite_tours: Mapped[list["FavoriteTours"]] = relationship(cascade="all, delete-orphan", lazy="subquery")
    # tours: Mapped[list["Tour"]] = relationship(back_populates="user", lazy="subquery")
    
