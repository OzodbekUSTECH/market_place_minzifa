from typing import Annotated
from fastapi import APIRouter, Depends
from services import support_questions_service
from schemas.support_questions import (
    CreateSupportQuestionSchema,
    UpdateSupportQuestionSchema,
    SupportQuestionSchema,
)
from schemas import IdResponseSchema
from repositories import Page
from utils.locale_handler import LocaleHandler
from database import UOWDependency

router = APIRouter(
    prefix="/support-questions",
    tags=["Support Question and Answer"],
)


@router.post('', response_model=IdResponseSchema)
async def create_support_question_answer(
    uow: UOWDependency,
    question_data: CreateSupportQuestionSchema
):
    return await support_questions_service.create_support_question(uow, question_data)

@router.get('/{locale}', response_model=Page[SupportQuestionSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_support_questions(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()]
):
    return await support_questions_service.get_list_of_questions(uow)

@router.get('/{locale}/{id}', response_model=SupportQuestionSchema)
async def get_support_question_answer_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    id: int    
):
    return await support_questions_service.get_question_by_id(uow, id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_support_qestion_answer(
    uow: UOWDependency,
    id: int,
    question_data: UpdateSupportQuestionSchema
):
    return await support_questions_service.update_question(uow, id, question_data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_support_question_answer(
    uow: UOWDependency,
    id: int
):
    return await support_questions_service.delete_question(uow, id)