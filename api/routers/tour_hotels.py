from schemas import IdResponseSchema
from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Form, Depends
import json
from utils.exceptions import CustomExceptions
from services import tour_hotels_service
from schemas.tour_hotels import CreateTourHotelSchema, UpdateTourHotelSchema, TourHotelSchema
from database import UOWDependency
from repositories import Page
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/tour-hotels",
    tags=["Tour Hotel and Media Group"],
)


@router.post("", response_model=IdResponseSchema)
async def create_tour_hotel(
    uow: UOWDependency,
    tour_id: int = Form(),
    name: str = Form(),
    description: str | None = Form(None),
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
        description_dict = json.loads(description) if description else None
        
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    
    hotel_data = CreateTourHotelSchema(
        tour_id=tour_id,
        name=name_dict,
        description=description_dict,
        stars=stars,
        photos=photos,
    )
    return await tour_hotels_service.create_hotel(uow, hotel_data)


@router.post("/media")
async def create_tour_hotel_media_group(uow: UOWDependency, tour_hotel_id: int, photos: list[UploadFile]):
    return await tour_hotels_service.create_hotel_media_group(uow, tour_hotel_id, photos)


@router.get('/{locale}/{tour_id}', response_model=Page[TourHotelSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_hotels_of_tour(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    tour_id: int,
):
    return await tour_hotels_service.get_hotels_of_tour(uow, tour_id)

@router.put("/{id}", response_model=IdResponseSchema)
async def update_tour_hotel(uow: UOWDependency, id: int, hotel_data: UpdateTourHotelSchema):
    return await tour_hotels_service.update_hotel(uow, id, hotel_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_tour_hotel(uow: UOWDependency, id: int):
    return await tour_hotels_service.delete_hotel(uow, id)


@router.delete("/media/{id}", response_model=IdResponseSchema)
async def delete_tour_hotel_photo(uow: UOWDependency, id: int):
    return await tour_hotels_service.delete_hotel_media(uow, id)
