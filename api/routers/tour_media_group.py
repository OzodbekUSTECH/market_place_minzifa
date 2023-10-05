from fastapi import APIRouter, UploadFile
from services import tour_media_group_service
from schemas import IdResponseSchema

router = APIRouter(
    prefix="/tour/media",
    tags=["Tour Media (photos/videos)"],
)


@router.post("", response_model=list[IdResponseSchema])
async def create_media_group_for_tour(tour_id: int, media_group: list[UploadFile]):
    return await tour_media_group_service.create_media_group(tour_id, media_group)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_media(id: int):
    return await tour_media_group_service.delete_media(id)
