from pydantic import BaseModel, EmailStr
from schemas import  CreateBaseModel, IdResponseSchema
from fastapi import UploadFile

class CreateEmailSchema(CreateBaseModel):
    name: str | None
    email: EmailStr
    language: str


class EmailSchema(CreateEmailSchema, IdResponseSchema):
    pass


class SendEmailMessageSchema(BaseModel):
    language: str
    subject: str
    body: str
    attachments: list[UploadFile] | None

