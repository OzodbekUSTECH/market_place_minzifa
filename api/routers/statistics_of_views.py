from fastapi import APIRouter, Depends
from services import statistics_of_views_service
from schemas.statistics_of_views import (
    StatisticOfViewsSchema
)
from database import UOWDependency


router = APIRouter(
    prefix="/statistics-views",
    tags=["Statistics of Views"],
)

@router.post('')
async def increase_statistics_views(
    uow: UOWDependency
):
    return await statistics_of_views_service.increase_statistics_views(uow)

@router.get('/pie-charts')
async def get_statistics_for_pie_charts(
    uow: UOWDependency
):
    return await statistics_of_views_service.get_percentage_statistics(uow)

@router.get('/line-graph', response_model=list[StatisticOfViewsSchema])
async def get_statistics_views_for_line_graph(
    uow: UOWDependency,
    start_date: str | None = None,
    end_date: str | None = None,
):
    return await statistics_of_views_service.get_statistics_by_period(uow, start_date, end_date)