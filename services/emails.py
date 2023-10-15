from schemas.emails import CreateEmailSchema, SendEmailMessageSchema
from repositories import paginate
from database import UnitOfWork, email_sender
from utils.exceptions import CustomExceptions
import models


class EmailsService:
    

    async def create_email(self, uow: UnitOfWork, email_data: CreateEmailSchema) -> models.Email:
        email_dict = email_data.model_dump()
        async with uow:
            existing_email = await uow.emails.get_by_email(email_data.email)
            if existing_email:
                raise CustomExceptions.conflict("You already subscribed!")
            email = await uow.emails.create(email_dict)
            await uow.commit()
            return email

    async def get_list_of_emails(self, uow: UnitOfWork, language: str | None) -> list[models.Email]:
        async with uow:
            if language:
                return paginate(await uow.emails.get_all_emails_by_language(
                    language, reverse=True
                ))
            return await uow.emails.get_all(reverse=True)

    
    async def get_email_by_id(self, uow: UnitOfWork, id: int) -> models.Email:
        async with uow:
            return await uow.emails.get_by_id(id)

    async def delete_email(self, uow: UnitOfWork,id: int) -> models.Email:
        async with uow:
            deleted_mail = await uow.emails.delete(id)
            await uow.commit()
            return deleted_mail

    async def send_message_to_emails(
        self,
        uow: UnitOfWork, 
        message_data: SendEmailMessageSchema
    ):
        async with uow:
            emails: list[
                models.Email
            ] = await uow.emails.get_all_emails_by_language(message_data.language)

            await email_sender.send_message_to_emails(
                emails=[data.email for data in emails], message_data=message_data
            )

            return {"message": "Message sent to all emails"}

emails_service = EmailsService()