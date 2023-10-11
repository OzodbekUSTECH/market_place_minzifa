from schemas import IdResponseSchema
from fastapi import APIRouter, UploadFile
from services import tour_hotels_service
from schemas.tour_hotels import CreateTourHotelSchema, UpdateTourHotelSchema

router = APIRouter(
    prefix="/tour-hotels",
    tags=["Tour Hotel and Media Group"],
)


@router.post("", response_model=IdResponseSchema)
async def create_tour_hotel(hotel_data: CreateTourHotelSchema):
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
