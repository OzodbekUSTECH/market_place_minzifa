from typing import Annotated
from fastapi import APIRouter, Depends, Request, UploadFile
from services import TourCommentsPhotosService
from utils.dependency import get_tour_comments_photos_services, get_current_user
from repositories.base import Pagination
from schemas.tour_comments_photos import TourCommentPhotoSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tours/comments/photos",
    tags=["Tour Comments Photos"]
)


@router.post('', response_model=list[TourCommentPhotoSchema])
async def create_tour_comment_photos(
    tour_comment_id: int,
    media_group: list[UploadFile],
    request: Request,
    tour_comments_photos_service: Annotated[TourCommentsPhotosService, Depends(get_tour_comments_photos_services)]
):
    return await tour_comments_photos_service.create_tour_comment_photos(request, tour_comment_id, media_group)

@router.get('', response_model=list[TourCommentPhotoSchema])
async def get_list_of_tour_comments_photos(
    pagination: Annotated[Pagination, Depends()],
    tour_comments_photos_service: Annotated[TourCommentsPhotosService, Depends(get_tour_comments_photos_services)]
):
    return await tour_comments_photos_service.get_list_of_tour_comments_photos(pagination)