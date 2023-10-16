from schemas.forms import (
    CreateCallBackFormSchema,
    CreateApplicationFormSchema,
    CreateAskQuestionFormSchema
)
from repositories import paginate
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models


class FormsService:

    async def create_call_back_form(self, uow: UnitOfWork, form_data: CreateCallBackFormSchema) -> models.CallBackForm:
        async with uow:
            call_back_form = await uow.call_back_forms.create(form_data.model_dump())
            await uow.commit()
            return call_back_form
    
    async def create_application_form(self, uow: UnitOfWork, form_data: CreateApplicationFormSchema) -> models.ApplicationForm:
        async with uow:
            application_form = await uow.application_forms.create(form_data.model_dump())
            await uow.commit()
            return application_form
        
    async def create_ask_question_form(self, uow: UnitOfWork, form_data: CreateAskQuestionFormSchema) -> models.AskQuestionForm:
        async with uow:
            ask_question_form = await uow.ask_question_forms.create(form_data.model_dump())
            await uow.commit()
            return ask_question_form
        
    async def get_call_back_forms(self, uow: UnitOfWork) -> list[models.CallBackForm]:
        async with uow:
            return await uow.call_back_forms.get_all(reverse=True)
        
    async def get_application_forms(self, uow: UnitOfWork) -> list[models.ApplicationForm]:
        async with uow:
            return await uow.application_forms.get_all(reverse=True)
        
    async def get_ask_question_forms(self, uow: UnitOfWork) -> list[models.AskQuestionForm]:
        async with uow:
            return await uow.application_forms.get_all(reverse=True)
        
    
    async def delete_call_back_form(self, uow: UnitOfWork, id: int) -> models.CallBackForm:
        async with uow:
            call_back_form: models.CallBackForm = await uow.call_back_forms.get_by_id(id)
            await uow.call_back_forms.delete(call_back_form.id)
            await uow.commit()
            return call_back_form
        
    async def delete_application_form(self, uow: UnitOfWork, id: int) -> models.ApplicationForm:
        async with uow:
            application_form: models.ApplicationForm = await uow.application_forms.get_by_id(id)
            await uow.application_forms.delete(application_form.id)
            await uow.commit()
            return application_form
        
    async def delete_ask_question_form(self, uow: UnitOfWork, id: int) -> models.AskQuestionForm:
        async with uow:
            ask_question_form: models.AskQuestionForm = await uow.ask_question_forms.get_by_id(id)
            await uow.ask_question_forms.delete(ask_question_form.id)
            await uow.commit()
            return ask_question_form
        

forms_service = FormsService()