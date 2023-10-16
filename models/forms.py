from models import BaseTable
from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

class BaseFormTable(BaseTable):
    __abstract__ = True

    name: Mapped[str]
    

class CallBackForm(BaseFormTable):
    __tablename__ = "call_back_forms"

    email: Mapped[str]
    phone_number: Mapped[str]

class ApplicationForm(BaseFormTable):
    __tablename__ = "application_forms"

    phone_number: Mapped[str]
    destination: Mapped[str]
    dates: Mapped[str]
    company_name: Mapped[str]
    price_per_participant: Mapped[float]
    amount_of_participants: Mapped[int]
    average_age: Mapped[float]

class AskQuestionForm(BaseFormTable):
    __tablename__ = "ask_question_forms"

    
    email: Mapped[str]
    question: Mapped[str] = mapped_column(Text)