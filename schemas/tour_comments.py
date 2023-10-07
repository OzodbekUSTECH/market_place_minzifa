from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema, TourMixinBaseModel
from pydantic import Field
from datetime import datetime
from typing import Union
from fastapi import UploadFile, File

class CustomTourSchema(IdResponseSchema):
    title: Union[dict[str, str], str]

class CustomUserSchema(IdResponseSchema):
    first_name: str
    last_name: str



class CreateCommentMediaSchema(CreateBaseModel):
    comment_id: int
    filename: str


class TourCommentMediaSchema(IdResponseSchema):
    comment_id: int
    media_url: str


############################
class CreateTourCommentSchema(TourMixinBaseModel, CreateBaseModel):
    user_id: int
    comment_text: str
    rating: float | None
    media: list[UploadFile] | None = Field(None, exclude=True)
    parent_comment_id: int | None



#############################
class UpdateTourCommentSchema(UpdateBaseModel, CreateTourCommentSchema):
    pass

#############################

class TourCommentReplySchema(IdResponseSchema, UpdateBaseModel):
    user: CustomUserSchema
    parent_comment_id: int
    comment_text: str




class TourCommentSchema(UpdateTourCommentSchema, IdResponseSchema):

    user: CustomUserSchema
    tour: CustomTourSchema
    media: list[TourCommentMediaSchema]
    replies: list[TourCommentReplySchema]


    tour_id: int = Field(exclude=True)
    user_id: int = Field(exclude=True)
    
