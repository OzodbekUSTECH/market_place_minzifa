from typing import Annotated
from fastapi import APIRouter, Depends, Request, UploadFile
from services import TourCommentsMediaService
from utils.dependency import get_tour_comments_media_services, get_current_user
from repositories.base import Pagination
from schemas.tour_comments_media import TourCommentMediaSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tours/comments/media",
    tags=["Tour Comments Media"]
)


@router.post('', response_model=list[TourCommentMediaSchema])
async def create_tour_comments_media(
    tour_comment_id: int,
    media_group: list[UploadFile],
    tour_comments_photos_service: Annotated[TourCommentsMediaService, Depends(get_tour_comments_media_services)]
):
    return await tour_comments_photos_service.create_tour_comments_media(tour_comment_id, media_group)



@router.get('/', response_model=list[TourCommentMediaSchema])
async def get_list_of_tour_comments_media(
    pagination: Annotated[Pagination, Depends()],
    tour_comments_photos_service: Annotated[TourCommentsMediaService, Depends(get_tour_comments_media_services)]
):
    return await tour_comments_photos_service.get_list_of_tour_comments_media(pagination)

@router.get('/comment/{tour_comment_id}', response_model=list[TourCommentMediaSchema])
async def get_list_of_tour_comments_media_by_tour_comment_id(
    tour_comment_id: int,
    tour_comments_photos_service: Annotated[TourCommentsMediaService, Depends(get_tour_comments_media_services)]
):
    return await tour_comments_photos_service.get_list_of_tour_comments_media_by_tour_comment_id(tour_comment_id)


@router.get('/{tour_comments_media_id}', response_model=TourCommentMediaSchema)
async def get_tour_comments_media_by_id(
    tour_comments_media_id: int,
    tour_comments_photos_service: Annotated[TourCommentsMediaService, Depends(get_tour_comments_media_services)]
):
    return await tour_comments_photos_service.get_tour_comments_media_by_id(tour_comments_media_id)



@router.put('/{tour_comments_media_id}', response_model=TourCommentMediaSchema)
async def update_tour_comments_media(
    tour_comments_media_id: int,
    media: UploadFile,
    tour_comments_photos_service: Annotated[TourCommentsMediaService, Depends(get_tour_comments_media_services)]
):
    return await tour_comments_photos_service.update_tour_comments_media(tour_comments_media_id, media)

@router.delete('/{tour_comments_media_id}', response_model=TourCommentMediaSchema)
async def delete_tour_comments_media(
    tour_comments_media_id: int,
    tour_comments_photos_service: Annotated[TourCommentsMediaService, Depends(get_tour_comments_media_services)]
):
    return await tour_comments_photos_service.delete_tour_comments_media(tour_comments_media_id)

