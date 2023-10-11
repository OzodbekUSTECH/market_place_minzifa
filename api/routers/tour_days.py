
from schemas import IdResponseSchema
from fastapi import APIRouter, UploadFile
from services import tour_days_service
from schemas.tour_days import (
    CreateTourDaySchema,

    UpdateTourDaySchema
)
router = APIRouter(
    prefix="/tour-days",
    tags=["Tour Days"],
)

@router.post('', response_model=IdResponseSchema)
async def create_tour_day(
    day_data: CreateTourDaySchema
):
    return await tour_days_service.create_tour_day(day_data)

@router.post('/media')
async def create_tour_day_media_group(
    tour_day_id: int,
    media_group: list[UploadFile]
):
    return await tour_days_service.create_tour_day_media_group(tour_day_id, media_group)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_tour_day(
    id: int,
    day_data: UpdateTourDaySchema
):
    return await tour_days_service.update_tour_day(id, day_data)


@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_tour_day(
    id: int
):
    return await tour_days_service.delete_tour_day(id)

@router.delete('/media/{id}', response_model=IdResponseSchema)
async def delete_tour_day_photo(
    id: int
):
    return await tour_days_service.delete_tour_day_media_group(id)

