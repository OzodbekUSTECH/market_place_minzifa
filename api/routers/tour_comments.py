from schemas.tour_comments import (
    CreateTourCommentSchema,
    UpdateTourCommentSchema,
    TourCommentSchema
)
from schemas import IdResponseSchema
from typing import Annotated
from fastapi import APIRouter, Depends, Form, UploadFile, File
from services import tour_comments_service
from repositories import Page
from utils.locale_handler import LocaleHandler
from utils.filters.filter_comments import FilterCommentsParams
from database import UOWDependency
router = APIRouter(
    prefix="/tour/comments",
    tags=["Tour Comments"],
)


@router.post("", response_model=IdResponseSchema)
async def create_tour_comment(
    uow: UOWDependency,
    tour_id: int = Form(),
    user_id: int = Form(),
    comment_text: str = Form(),
    rating: float | None = Form(None, ge=1, le=5),
    photo_1: UploadFile = File(None),
    photo_2: UploadFile = File(None),
    photo_3: UploadFile = File(None),
    parent_comment_id: int = Form(None),
):
    media = [file for file in [photo_1, photo_2, photo_3] if file is not None]

    comment_data = CreateTourCommentSchema(
        tour_id=tour_id,
        user_id=user_id,
        comment_text=comment_text,
        rating=rating,
        media=media,
        parent_comment_id=parent_comment_id
    )
    return await tour_comments_service.create_comment(uow, comment_data)

@router.post('/media/{comment_id}')
async def create_comment_media(
    uow: UOWDependency,
    comment_id: int,
    media_group: list[UploadFile]
) -> None:
    
    await tour_comments_service.create_media(uow, comment_id, media_group)



@router.get("/{locale}", response_model=Page[TourCommentSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_tour_comments(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    filter_params: Annotated[FilterCommentsParams, Depends()]
):
    return await tour_comments_service.get_list_of_comments(uow, filter_params)


@router.get("/{locale}/{id}", response_model=TourCommentSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_tour_comment_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    id: int
):
    return await tour_comments_service.get_comment_by_id(uow, id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_tour_comment(
    uow: UOWDependency,
    id: int,
    tour_id: int = Form(),
    user_id: int = Form(),
    comment_text: str = Form(),
    rating: float | None = Form(None, ge=1, le=5),
    parent_comment_id: int = Form(None),
):
    comment_data = UpdateTourCommentSchema(
        tour_id=tour_id,
        user_id=user_id,
        comment_text=comment_text,
        rating=rating,
        parent_comment_id=parent_comment_id
    )
    return await tour_comments_service.update_comment(uow, id, comment_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_tour_comment(uow: UOWDependency, id: int):
    return await tour_comments_service.delete_comment(uow, id)


@router.delete('/media/{id}', response_model=IdResponseSchema)
async def delete_tour_comment_media(
    uow: UOWDependency,
    id: int
):
    return await tour_comments_service.delete_media(uow, id)


