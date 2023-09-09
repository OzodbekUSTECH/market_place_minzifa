from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

    
class CreateMailListSchema(BaseModel):
    name: Optional[str] = None
    email: EmailStr

class UpdateMailListSchema(CreateMailListSchema):
    updated_at: datetime = None

class MailListSchema(CreateMailListSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    


class SendMailMessageSchema(BaseModel):
    subject: str
    body: str