from fastapi import APIRouter, UploadFile
from services import tour_media_group_service
from schemas import IdResponseSchema
from database import UOWDependency

router = APIRouter(
    prefix="/tour/media",
    tags=["Tour Media (photos/videos)"],
)


@router.post("")
async def create_media_group_for_tour(uow: UOWDependency, tour_id: int, media_group: list[UploadFile]):
    return await tour_media_group_service.create_media_group(uow, tour_id, media_group)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_media(uow: UOWDependency, id: int):
    return await tour_media_group_service.delete_media(uow, id)
