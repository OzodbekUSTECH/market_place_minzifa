from schemas import IdResponseSchema
from fastapi import APIRouter
from repositories import Page
from services import tour_importants_service
from schemas.tour_importants import (
    CreateTourImportantSchema,
    UpdateTourImportantSchema,
)
from database import UOWDependency

router = APIRouter(
    prefix="/tour-importants",
    tags=["Tour Importants to know"],
)

@router.post('', response_model=IdResponseSchema)
async def create_tour_important_info_to_know(
    uow: UOWDependency,
    data: CreateTourImportantSchema
):
    return await tour_importants_service.create_tour_important(uow, data)

@router.put('/{id}',response_model=IdResponseSchema)
async def update_tour_important_info_to_know(
    uow: UOWDependency,
    id: int, 
    data: UpdateTourImportantSchema
):
    return await tour_importants_service.update_tour_important(uow, id, data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_tour_important_info_to_know(uow: UOWDependency, id: int):
    return await tour_importants_service.delete_tour_important(uow, id)