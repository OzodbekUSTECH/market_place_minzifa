from schemas.tour_comments import (
    CreateTourCommentSchema,
    UpdateTourCommentSchema,
    TourCommentSchema
)
from schemas import IdResponseSchema
from typing import Annotated
from fastapi import APIRouter, Depends, Form, UploadFile, File
from services import tour_days_service
from repositories import Page
from utils.filters.filter_comments import FilterCommentsParams
from typing import Optional, Union
router = APIRouter(
    prefix="/tour-days",
    tags=["Tour Days"],
)

@router.delete('', response_model=IdResponseSchema)
async def delete_tour_day(
    id: int
):
    return await tour_days_service.delete_tour_day(id)

