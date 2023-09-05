from pydantic import BaseModel

class CreateLanguageSchema(BaseModel):
    name: str

class UpdateLanguageSchema(CreateLanguageSchema):
    pass

class LanguageSchema(CreateLanguageSchema):
    id: int