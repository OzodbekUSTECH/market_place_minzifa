from repositories import Pagination
from schemas.support_questions import (
    CreateSupportQuestionSchema, 
    CreateQuestionDocSchema, 
    UpdateSupportQuestionSchema, 
    UpdateQuestionDocSchema
)
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class SupportQuestionsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_support_question(self, question_data: CreateSupportQuestionSchema) -> models.SupportQuestion:
        question_dict = question_data.model_dump()
        async with self.uow:
            support_question: models.SupportQuestion = await self.uow.support_questions.create(question_dict)

            if question_data.doc_links:
                await self.uow.question_docs.bulk_create(
                    data_list=[CreateQuestionDocSchema(
                        question_id=support_question.id,
                        link= doc_link
                    ).model_dump() for doc_link in question_data.doc_links]
                )

            await self.uow.commit()

            return support_question
        
    async def get_list_of_questions(self) -> list[models.SupportQuestion]:
        async with self.uow:
            return await self.uow.support_questions.get_all()

    async def get_question_by_id(self, id: int) -> models.SupportQuestion:
        async with self.uow:
            return await self.uow.support_questions.get_by_id(id)
    

    async def _update_items(
        self, 
        current_items: set[str], 
        new_items: set[str], 
        add_item_func: callable, 
        remove_item_func: callable, 
    ):
        items_to_add = new_items - current_items
        items_to_remove = current_items - new_items
        
        for item_id in items_to_add:
            await add_item_func(item_id)
        
        for item_id in items_to_remove:
            await remove_item_func(item_id)



    async def update_question(self, id: int, question_data: UpdateSupportQuestionSchema) -> models.SupportQuestion:
        async with self.uow:
            existing_question: models.SupportQuestion = await self.uow.support_questions.get_by_id(id)

            if not existing_question:
                raise CustomExceptions.not_found()
            
            if question_data.doc_links is None:
                # If doc_links is None, remove all existing links
                for doc_link in existing_question.question_doc_links:
                    await self.uow.question_docs.delete_by(
                        question_id=existing_question.id,
                        link=doc_link
                    )
            else:
                await self._update_items(
                    set(existing_question.question_doc_links),
                    set(question_data.doc_links),
                    lambda doc_link: self.uow.question_docs.create(
                        CreateQuestionDocSchema(
                            question_id=existing_question.id,
                            link=doc_link
                        ).model_dump()
                    ),
                    lambda doc_link: self.uow.question_docs.delete_by(
                        question_id=existing_question.id,
                        link=doc_link
                    )
                )

            question_dict = question_data.model_dump()
            
            updated_support_question = await self.uow.support_questions.update(id, question_dict)

            await self.uow.commit()
            return updated_support_question

        
    async def delete_question(self, id: int) -> models.SupportQuestion:
        async with self.uow:
            question = await self.uow.support_questions.delete(id)
            await self.uow.commit()
            return question
            
            

support_questions_service = SupportQuestionsService()