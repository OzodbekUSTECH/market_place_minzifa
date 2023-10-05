from models import BaseTable
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.hybrid import hybrid_property

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import User

class QuestionDoc(BaseTable):
    __tablename__ = 'question_docs'

    question_id: Mapped[int] = mapped_column(ForeignKey("support_questions.id", ondelete='CASCADE'))
    link: Mapped[str]

class SupportQuestion(BaseTable):
    __tablename__ = 'support_questions'

    question: Mapped[dict] = mapped_column(type_=JSONB)
    answer: Mapped[dict] = mapped_column(type_=JSONB)

    @hybrid_property
    def question_doc_links(self) -> list[str]:
        return [doc.link for doc in self.doc_links]

    doc_links: Mapped[list["QuestionDoc"]] = relationship(lazy="subquery", cascade="all, delete-orphan")



