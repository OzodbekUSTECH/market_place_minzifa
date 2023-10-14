from schemas import IdResponseSchema
from fastapi import APIRouter
from repositories import Page
from services import accommodation_types_service
from schemas.accommodation_types import (
    CreateAccommodationTypeSchema,
    UpdateAccommodationTypeSchema,
    AccommodationTypeSchema,
)

router = APIRouter(
    prefix="/accommodation-types",
    tags=["Accommodation Types (single, double room ... etc)"],
)

@router.post('', response_model=IdResponseSchema)
async def create_accommodation_type(
    type_data: CreateAccommodationTypeSchema
):
    return await accommodation_types_service.create_type(type_data)

@router.get('', response_model=Page[AccommodationTypeSchema])
async def get_accommodation_types():
    return await accommodation_types_service.get_types()

@router.get("/{id}", response_model=AccommodationTypeSchema)
async def get_accommodation_type_by_id(id: int):
    return await accommodation_types_service.get_type_by_id(id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_accommodation_type(
    id: int,
    type_data: UpdateAccommodationTypeSchema
):
    return await accommodation_types_service.update_type(id, type_data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_accommodation_type(id: int):
    return await accommodation_types_service.delete_type(id)
    

