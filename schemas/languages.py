from pydantic import BaseModel
from typing import Union
class CreateLanguageSchema(BaseModel):
    name: Union[dict[str, str], str]

class UpdateLanguageSchema(CreateLanguageSchema):
    pass

class LanguageSchema(CreateLanguageSchema):
    id: int