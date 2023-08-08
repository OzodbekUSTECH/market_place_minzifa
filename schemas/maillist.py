from pydantic import BaseModel, EmailStr
from typing import Optional


    
class CreateMailListSchema(BaseModel):
    name: str = None
    email: EmailStr

class UpdateMailListSchema(CreateMailListSchema):
    pass

class MailListSchema(BaseModel):
    id: int
    name: Optional[str]
    email: EmailStr

    class Config:
        from_attribute = True


class SendMailMessageSchema(BaseModel):
    subject: str
    body: str