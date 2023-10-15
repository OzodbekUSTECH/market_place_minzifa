from schemas import IdResponseSchema
from fastapi import APIRouter, UploadFile, File, Form
import json
from utils.exceptions import CustomExceptions
from services import tour_hotels_service
from schemas.tour_hotels import CreateTourHotelSchema, UpdateTourHotelSchema
from database import UOWDependency

router = APIRouter(
    prefix="/tour-hotels",
    tags=["Tour Hotel and Media Group"],
)


@router.post("", response_model=IdResponseSchema)
async def create_tour_hotel(
    uow: UOWDependency,
    tour_id: int = Form(),
    name: str = Form(),
    short_description: str | None = Form(None),
    stars: int | None = Form(None),
    photos: list[UploadFile] = File()
):
    """
    For example:
    - form data name: {"en": "string", "ru": "string"}
    - form data short_description: {"en": "string", "ru": "string"}
    """
    try:
        name_dict = json.loads(name)
        short_description_dict = json.loads(short_description) if short_description else None
        
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    
    hotel_data = CreateTourHotelSchema(
        tour_id=tour_id,
        name=name_dict,
        short_description=short_description_dict,
        stars=stars,
        photos=photos,
    )
    return await tour_hotels_service.create_hotel(uow, hotel_data)


@router.post("/media")
async def create_tour_hotel_media_group(uow: UOWDependency, tour_hotel_id: int, photos: list[UploadFile]):
    return await tour_hotels_service.create_hotel_media_group(uow, tour_hotel_id, photos)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_tour_hotel(uow: UOWDependency, id: int, hotel_data: UpdateTourHotelSchema):
    return await tour_hotels_service.update_hotel(uow, id, hotel_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_tour_hotel(uow: UOWDependency, id: int):
    return await tour_hotels_service.delete_hotel(uow, id)


@router.delete("/media/{id}", response_model=IdResponseSchema)
async def delete_tour_hotel_photo(uow: UOWDependency, id: int):
    return await tour_hotels_service.delete_hotel_media(uow, id)
