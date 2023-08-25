from typing import Annotated
from fastapi import APIRouter, Depends
from services import ToursService
from utils.dependency import get_tours_services, get_current_user
from repositories import Pagination
from schemas.tours import CreateTourPriceSchema, UpdateTourPriceSchema, CreateTourSchema, UpdateTourSchema, TourSchema, TourPriceSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tours",
    tags=["Tours"],
)


@router.post('')
async def create_tour(
    tour_data: CreateTourSchema,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
):
    return await tours_service.create_tour(tour_data)

@router.get('')
async def get_list_of_tours(
    pagination: Annotated[Pagination, Depends()],
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
):
    return await tours_service.get_list_of_tours(pagination)