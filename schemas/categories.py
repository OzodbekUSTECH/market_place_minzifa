from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateCategorySchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateCategorySchema(UpdateBaseModel, CreateCategorySchema):
    pass

class CategorySchema(IdResponseSchema, UpdateCategorySchema):
    pass