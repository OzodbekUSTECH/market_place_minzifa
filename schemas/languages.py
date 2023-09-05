from pydantic import BaseModel

class CreateLanguageSchema(BaseModel):
    tour_id: int
    language_id: int

class UpdateLanguageSchema(CreateLanguageSchema):
    pass

class LanguageSchema(CreateLanguageSchema):
    id: int