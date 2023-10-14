from schemas import IdResponseSchema
from fastapi import APIRouter, UploadFile, File, Form
import json
from utils.exceptions import CustomExceptions
from services import tour_hotels_service
from schemas.tour_hotels import CreateTourHotelSchema, UpdateTourHotelSchema

router = APIRouter(
    prefix="/tour-hotels",
    tags=["Tour Hotel and Media Group"],
)


@router.post("", response_model=IdResponseSchema)
async def create_tour_hotel(
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
        short_description_dict = json.loads(short_description)
        
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    
    hotel_data = CreateTourHotelSchema(
        name=name_dict,
        short_description=short_description_dict,
        stars=stars,
        photos=photos,
    )
    return await tour_hotels_service.create_hotel(hotel_data)


@router.post("/media")
async def create_tour_hotel_media_group(tour_hotel_id: int, photos: list[UploadFile]):
    return await tour_hotels_service.create_hotel_media_group(tour_hotel_id, photos)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_tour_hotel(id: int, hotel_data: UpdateTourHotelSchema):
    return await tour_hotels_service.update_hotel(id, hotel_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_tour_hotel(id: int):
    return await tour_hotels_service.delete_hotel(id)


@router.delete("/media/{id}", response_model=IdResponseSchema)
async def delete_tour_hotel_photo(id: int):
    return await tour_hotels_service.delete_hotel_media(id)
