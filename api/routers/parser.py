from schemas.orders import (
    CreateOrderSchema,
    UpdateOrderSchema,
    OrderSchema
)
from typing import Annotated
from fastapi import APIRouter, Depends, BackgroundTasks
from services import parser_service
from repositories import Page
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from utils.filters.filter_orders import FilterOrderParams
from database import UOWDependency

router = APIRouter(
    prefix="/parser",
    tags=["Parser"],
)

@router.post('/countries-regions')
async def parse_countries_and_regions(bg: BackgroundTasks):
    bg.add_task(parser_service.parse_countries_and_regions)

@router.post('/types')
async def parse_types(bg: BackgroundTasks):
    bg.add_task(parser_service.parse_types)

@router.post('/tours')
async def parse_tours(bg: BackgroundTasks):
    bg.add_task(parser_service.parse_tours)

@router.post('/tour-days')
async def parse_tour_days(bg: BackgroundTasks):
    bg.add_task(parser_service.parse_tour_days)

@router.post('/tour-hotels')
async def parse_tour_hotels(bg: BackgroundTasks):
    bg.add_task(parser_service.parse_hotels)

@router.post('/tour-in-excludes')
async def parse_tour_in_excludes(bg: BackgroundTasks):
    bg.add_task(parser_service.parse_includes_and_excludes)

@router.post('/tour-imporants')
async def parse_tour_imporants(bg: BackgroundTasks):
    bg.add_task(parser_service.parse_importants)

