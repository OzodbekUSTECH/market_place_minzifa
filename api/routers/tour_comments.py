from schemas.tour_comments import CreateTourCommentSchema, UpdateTourCommentSchema, TourCommentSchema
from typing import Annotated
from fastapi import APIRouter, Depends
from services import TourCommentsService
from utils.dependency import get_tour_comments_services, get_current_user
from repositories import Pagination
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tour/comments",
    tags=["Tour Comments"],
)


@router.post('', response_model=TourCommentSchema)
async def create_tour_comment(
    tour_comment_data: CreateTourCommentSchema,
    tour_comments_service: Annotated[TourCommentsService, Depends(get_tour_comments_services)]
) -> TourCommentSchema:
    return await tour_comments_service.create_tour_comment(tour_comment_data)

@router.get('', response_model=list[TourCommentSchema])
async def get_list_of_tour_comments(
    pagination: Annotated[Pagination, Depends()],
    tour_comments_service: Annotated[TourCommentsService, Depends(get_tour_comments_services)]
) -> list[TourCommentSchema]:
    return await tour_comments_service.get_list_of_tour_comments(pagination)

@router.get('/{id}', response_model=TourCommentSchema)
async def get_tour_comment_by_id(
    id: int,
    tour_comments_service: Annotated[TourCommentsService, Depends(get_tour_comments_services)]
) -> TourCommentSchema:
    return await tour_comments_service.get_tour_comment_by_id(id)

@router.get('/tour/{tour_id}', response_model=list[TourCommentSchema])
async def get_list_of_comments_of_tour(
    tour_id: int,
    pagination: Annotated[Pagination, Depends()],
    tour_comments_service: Annotated[TourCommentsService, Depends(get_tour_comments_services)]
) -> list[TourCommentSchema]:
    return await tour_comments_service.get_list_of_comments_of_tour(tour_id, pagination)

@router.put('/{id}', response_model=TourCommentSchema)
async def update_tour_comment(
    id: int,
    tour_comment_data: UpdateTourCommentSchema,
    tour_comments_service: Annotated[TourCommentsService, Depends(get_tour_comments_services)]
) -> TourCommentSchema:
    return await tour_comments_service.update_tour_comment(id, tour_comment_data)

@router.delete('/{id}', response_model=TourCommentSchema)
async def delete_tour_comment(
    id: int,
    tour_comments_service: Annotated[TourCommentsService, Depends(get_tour_comments_services)]
):
    return await tour_comments_service.delete_tour_comment(id)