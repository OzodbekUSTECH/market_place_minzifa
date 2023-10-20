
from schemas import IdResponseSchema
from fastapi import APIRouter, UploadFile, File, Form
import json
from utils.exceptions import CustomExceptions
from services import tour_days_service
from schemas.tour_days import (
    CreateTourDaySchema,

    UpdateTourDaySchema
)
from database import UOWDependency

router = APIRouter(
    prefix="/tour-days",
    tags=["Tour Days"],
)

@router.post('', response_model=IdResponseSchema)
async def create_tour_day(
    uow: UOWDependency, 
    tour_id: int = Form(),
    day: int = Form(),
    name: str = Form(),
    description: str = Form(),
    region_id: str | None = Form(None),
    photo_1: UploadFile = File(None),
    photo_2: UploadFile = File(None),
    photo_3: UploadFile = File(None)
):
    """
    For example:
    - form data name: {"en": "string", "ru": "string"}
    - form data description: {"en": "string", "ru": "string"}
    """
    try:
        name_dict = json.loads(name)
        description_dict = json.loads(description)
        
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    
    photos = [file for file in [photo_1, photo_2, photo_3] if file is not None]
    day_data = CreateTourDaySchema(
        tour_id=tour_id,
        day = day,
        name=name_dict,
        description=description_dict,
        region_id=region_id,
        photos=photos
    )
    return await tour_days_service.create_tour_day(uow, day_data)

@router.post('/media')
async def create_tour_day_media_group(
    uow: UOWDependency,
    tour_day_id: int,
    media_group: list[UploadFile]
):
    return await tour_days_service.create_tour_day_media_group(uow, tour_day_id, media_group)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_tour_day(
    uow: UOWDependency,
    id: int,
    day_data: UpdateTourDaySchema
):
    return await tour_days_service.update_tour_day(uow, id, day_data)


@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_tour_day(
    uow: UOWDependency,
    id: int
):
    return await tour_days_service.delete_tour_day(uow, id)

@router.delete('/media/{id}', response_model=IdResponseSchema)
async def delete_tour_day_photo(
    uow: UOWDependency,
    id: int
):
    return await tour_days_service.delete_tour_day_media_group(uow, id)

