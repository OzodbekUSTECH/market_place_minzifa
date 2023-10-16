from schemas import  CreateBaseModel, IdResponseSchema
from pydantic import EmailStr
class BaseFormModel(CreateBaseModel):
    name: str

class CreateCallBackFormSchema(BaseFormModel):
    email: EmailStr
    phone_number: str

class CreateApplicationFormSchema(BaseFormModel):
    phone_number: str
    destination: str
    dates: str
    company_name: str
    price_per_participant: float
    amount_of_participants: int
    average_age: float

class CreateAskQuestionFormSchema(BaseFormModel):
    email: EmailStr
    question: str

################################

class CallBackFormSchema(CreateCallBackFormSchema):
    pass

class ApplicationFormSchema(CreateApplicationFormSchema):
    pass

class AskQuestionFormSchema(CreateAskQuestionFormSchema):
    pass