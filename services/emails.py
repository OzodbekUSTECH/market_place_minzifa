from schemas.emails import CreateEmailSchema, SendEmailMessageSchema
from repositories import paginate
from database import UnitOfWork, email_sender
from utils.exceptions import CustomExceptions
import models


class EmailsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_email(self, email_data: CreateEmailSchema) -> models.Email:
        email_dict = email_data.model_dump()
        async with self.uow:
            existing_email = await self.uow.emails.get_by_email(email_data.email)
            if existing_email:
                raise CustomExceptions.conflict("You already subscribed!")
            email = await self.uow.emails.create(email_dict)
            await self.uow.commit()
            return email

    async def get_list_of_emails(self, language: str | None) -> list[models.Email]:
        async with self.uow:
            if language:
                return paginate(await self.uow.emails.get_all_emails_by_language(
                    language, reverse=True
                ))
            return await self.uow.emails.get_all(reverse=True)

    
    async def get_email_by_id(self, id: int) -> models.Email:
        async with self.uow:
            return await self.uow.emails.get_by_id(id)

    async def delete_email(self, id: int) -> models.Email:
        async with self.uow:
            deleted_mail = await self.uow.emails.delete(id)
            await self.uow.commit()
            return deleted_mail

    async def send_message_to_emails(
        self, message_data: SendEmailMessageSchema
    ):
        async with self.uow:
            emails: list[
                models.Email
            ] = await self.uow.emails.get_all_emails_by_language(message_data.language)

            await email_sender.send_message_to_emails(
                emails=[data.email for data in emails], message_data=message_data
            )

            return {"message": "Message sent to all emails"}

emails_service = EmailsService()