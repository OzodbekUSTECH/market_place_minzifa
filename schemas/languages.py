from typing import Union
from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema

class CreateLanguageSchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateLanguageSchema(CreateLanguageSchema, UpdateBaseModel):
    pass

class LanguageSchema(UpdateLanguageSchema, IdResponseSchema):
    pass