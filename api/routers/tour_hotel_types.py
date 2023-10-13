from schemas import IdResponseSchema
from fastapi import APIRouter, UploadFile
from repositories import Page
from services import tour_hotel_types_service
from schemas.tour_hotels import CreateTourHotelTypeSchema, UpdateTourHotelTypeSchema, TourHotelTypeSchema

router = APIRouter(
    prefix="/hotel-types",
    tags=["Tour Hotel Type (single ... etc)"],
)

@router.post('', response_model=IdResponseSchema)
async def create_tour_hotel_type(
    type_data: CreateTourHotelTypeSchema
):
    return await tour_hotel_types_service.create_hotel_type(type_data)

@router.get('', response_model=Page[TourHotelTypeSchema])
async def get_tour_hotel_types():
    return await tour_hotel_types_service.get_hotel_types()

@router.get("/{id}", response_model=TourHotelTypeSchema)
async def get_tour_hotel_type_by_id(id: int):
    return await tour_hotel_types_service.get_hotel_type_by_id(id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_tour_hotel_type(
    id: int,
    type_data: UpdateTourHotelTypeSchema
):
    return await tour_hotel_types_service.update_hotel_type(id, type_data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_tour_hotel(id: int):
    return await tour_hotel_types_service.delete_hotel_type(id)
    

