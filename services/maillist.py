from schemas.maillist import CreateMailListSchema, UpdateMailListSchema, MailListSchema
from repositories import Pagination
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from models import MailList

class MailListService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def subscribe(self, mail_data: CreateMailListSchema) -> MailList:
        mail_dict = mail_data.model_dump()

        async with self.uow:
            existing_email = await self.uow.maillist.get_by_email(mail_data.email)
            if existing_email:
                raise CustomExceptions.conflict("You already subscribed!")
            created_mail = await self.uow.maillist.create(mail_dict)
            
            return created_mail
    
    async def get_all_mails(self, pagination: Pagination) -> list[MailList]:
        async with self.uow:
            all_mails = await self.uow.maillist.get_all(pagination)
            
            return all_mails
    
    async def get_mail_by_id(self, mail_id: int) -> MailList:
        async with self.uow:
            mail = await self.uow.maillist.get_by_id(mail_id)
            
            return mail
    
    async def get_emails_without_pagination(self) -> list[MailList]:
        async with self.uow:
            all_mails = await self.uow.maillist.get_all_emails_without_pagination()
            
            return all_mails
    
    async def update_email(self, mail_id: int, email_data: UpdateMailListSchema) -> MailList:
        email_dict = email_data.model_dump()
        async with self.uow:
            updated_mail = await self.uow.maillist.update(mail_id, email_dict)
            

            return updated_mail
    
    async def delete_email(self, mail_id: int) -> MailList:
        async with self.uow:
            deleted_mail = await self.uow.maillist.delete(mail_id)
            
            return deleted_mail