from typing import Annotated
from fastapi import APIRouter, Depends, Form, UploadFile, File
from services import forms_service
from repositories import Page
from schemas.forms import (
    CreateCallBackFormSchema,
    CreateApplicationFormSchema,
    CreateAskQuestionFormSchema,

    CallBackFormSchema,
    ApplicationFormSchema,
    AskQuestionFormSchema
    
)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
import json
from utils.exceptions import CustomExceptions
from database import UOWDependency

router = APIRouter(
    prefix="/forms",
    tags=["Forms (call back, application, ask yout qestion)"],
)

@router.post('/call-back', response_model=IdResponseSchema)
async def create_call_back_form(
    uow: UOWDependency,
    form_data: CreateCallBackFormSchema
):
    return await forms_service.create_call_back_form(uow, form_data)

@router.post('/application', response_model=IdResponseSchema)
async def create_application_form(
    uow: UOWDependency,
    form_data: CreateApplicationFormSchema,
):
    return await forms_service.create_application_form(uow, form_data)

@router.post('/ask-question', response_model=IdResponseSchema)
async def create_ask_your_question(
    uow: UOWDependency,
    form_data: CreateAskQuestionFormSchema,
):
    return await forms_service.create_ask_question_form(uow, form_data)

@router.get('/call-back', response_model=Page[CallBackFormSchema])
async def get_call_back_forms(
    uow: UOWDependency,
):
    return await forms_service.get_call_back_forms(uow)

@router.get('/application', response_model=Page[ApplicationFormSchema])
async def get_application_forms(
    uow: UOWDependency,
):
    return await forms_service.get_application_forms(uow)

@router.get('/ask-question', response_model=Page[AskQuestionFormSchema])
async def get_ask_your_question_forms(
    uow: UOWDependency,
):
    return await forms_service.get_ask_question_forms(uow)

@router.delete('/call-back/{id}', response_model=IdResponseSchema)
async def delete_call_back_form(
    uow: UOWDependency,
    id: int
):
    return await forms_service.delete_call_back_form(uow, id)

@router.delete('/application/{id}', response_model=IdResponseSchema)
async def delete_application_form(
    uow: UOWDependency,
    id: int
):
    return await forms_service.delete_application_form(uow, id)

@router.delete('/ask-question/{id}', response_model=IdResponseSchema)
async def delete_ask_your_question_form(
    uow: UOWDependency,
    id: int
):
    return await forms_service.delete_ask_question_form(uow, id)