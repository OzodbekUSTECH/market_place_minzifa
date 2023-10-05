from typing import Annotated
from fastapi import APIRouter, Depends
from services import TourPricesService
from utils.dependency import get_tour_prices_services, get_current_user
from repositories import Pagination
from schemas.tour_prices import (
    CreateTourPriceSchema,
    UpdateTourPriceSchema,
    TourPriceSchema,
)
from schemas import IdResponseSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tour/prices",
    tags=["Tour Prices"],
)


@router.post("", response_model=list[IdResponseSchema])
async def create_tour_prices(
    price_data: CreateTourPriceSchema,
    tour_prices_service: Annotated[
        TourPricesService, Depends(get_tour_prices_services)
    ],
) -> list[TourPriceSchema]:
    return await tour_prices_service.create_tour_prices(price_data)


@router.get("", response_model=list[TourPriceSchema])
async def get_list_of_prices(
    pagination: Annotated[Pagination, Depends()],
    tour_prices_service: Annotated[
        TourPricesService, Depends(get_tour_prices_services)
    ],
) -> list[TourPriceSchema]:
    return await tour_prices_service.get_list_of_prices(pagination)


@router.get("/tour/{tour_id}", response_model=list[TourPriceSchema])
async def get_list_of_prices_of_tour(
    tour_id: int,
    tour_prices_service: Annotated[
        TourPricesService, Depends(get_tour_prices_services)
    ],
) -> list[TourPriceSchema]:
    return await tour_prices_service.get_list_of_prices_of_tour(tour_id)


@router.get("/{id}", response_model=TourPriceSchema)
async def get_tour_price_by_id(
    id: int,
    tour_prices_service: Annotated[
        TourPricesService, Depends(get_tour_prices_services)
    ],
) -> TourPriceSchema:
    return await tour_prices_service.get_price_by_id(id)


@router.put("", response_model=list[IdResponseSchema])
async def update_tour_prices(
    tour_data: UpdateTourPriceSchema,
    tour_prices_service: Annotated[
        TourPricesService, Depends(get_tour_prices_services)
    ],
) -> list[TourPriceSchema]:
    return await tour_prices_service.update_tour_prices(tour_data)
