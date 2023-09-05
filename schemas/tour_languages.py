from pydantic import BaseModel

class CreateTourLanguageSchema(BaseModel):
    tour_id: int
    language_id: int

class UpdateTourLanguageSchema(CreateTourLanguageSchema):
    pass

class TourLanguageSchema(CreateTourLanguageSchema):
    id: int