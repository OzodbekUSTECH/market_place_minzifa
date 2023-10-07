from fastapi import APIRouter, Depends
from services import statistics_of_views_service
from schemas.statistics_of_views import (
    StatisticOfViewsSchema
)


router = APIRouter(
    prefix="/statistics-views",
    tags=["Statistics of Views"],
)

@router.post('')
async def increase_statistics_views():
    return await statistics_of_views_service.increase_statistics_views()

@router.get('/pie-charts')
async def get_statistics_for_pie_charts():
    return await statistics_of_views_service.get_percentage_statistics()

@router.get('/line-graph', response_model=list[StatisticOfViewsSchema])
async def get_statistics_views_for_line_graph(
    start_date: str | None = None,
    end_date: str | None = None,
):
    return await statistics_of_views_service.get_statistics_by_period(start_date, end_date)