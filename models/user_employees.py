from models import BaseTable
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class UserEmployee(BaseTable):
    __tablename__ = 'user_employees'
    
    travel_expert_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    employee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    