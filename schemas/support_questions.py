from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from pydantic import Field
from typing import Union

class CreateQuestionDocSchema(CreateBaseModel):
    question_id: int
    link: str

class UpdateQuestionDocSchema(CreateQuestionDocSchema, UpdateBaseModel):
    pass

class QuestionDocSchema(UpdateQuestionDocSchema, IdResponseSchema):
    pass
    

class CreateSupportQuestionSchema(CreateBaseModel):
    question: Union[dict[str, str], str]
    answer: Union[dict[str, str], str]
    doc_links: list[str] | None = Field(None, exclude=True)

class UpdateSupportQuestionSchema(CreateSupportQuestionSchema, UpdateBaseModel):
    pass

class SupportQuestionSchema(UpdateSupportQuestionSchema, IdResponseSchema):
    doc_links: list[QuestionDocSchema]

