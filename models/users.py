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

    @hybrid_property
    def rating(self):
        total_rating = 0
        amount_reviews = 0

        if self.tours:
            for tour in self.tours:
                total_rating += tour.rating # Учтем максимальное значение рейтинга
                amount_reviews += tour.amount_reviews

        if amount_reviews == 0:
            return 1  # Возвращаем значение по умолчанию (1) если нет комментариев с рейтингом
        else:
            return round(total_rating / amount_reviews, 2)
        
    @hybrid_property
    def amount_reviews(self) -> int:
        default = 0
        if self.tours:
            for tour in self.tours:
                default += tour.amount_reviews
        
        return default



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
    tours: Mapped[list["Tour"]] = relationship(
        back_populates="user", 
        lazy="subquery",
        primaryjoin="User.id == Tour.user_id",
    )
    leader_tours: Mapped[list["Tour"]] = relationship(
        back_populates="tour_leader", 
        lazy="subquery",
        primaryjoin="User.id == Tour.tour_leader_id"
    )
    
    
    
