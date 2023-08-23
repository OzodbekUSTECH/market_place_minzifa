from repositories.maillist import MailListRepository
from schemas.maillist import CreateMailListSchema, UpdateMailListSchema, MailListSchema
from fastapi import HTTPException, status
from repositories.base import Pagination
from repositories.unitofwork import UnitOfWork


class MailListService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def subscribe(self, mail_data: CreateMailListSchema) -> MailListSchema:
        mail_dict = mail_data.model_dump()

        async with self.uow:
            existing_email = await self.uow.maillist.get_by_email(mail_data.email)
            if existing_email:
                raise HTTPException(status_code=status.HTTP_200_OK, detail="You already subscribed!")
            created_mail = await self.uow.maillist.create(mail_dict)
            await self.uow.commit()
            return created_mail
    
    async def get_all_mails(self, pagination: Pagination) -> list[MailListSchema]:
        async with self.uow:
            all_mails = await self.uow.maillist.get_all(pagination)
            await self.uow.commit()
            return all_mails
    
    async def get_mail_by_id(self, mail_id: int) -> MailListSchema:
        async with self.uow:
            mail = await self.uow.maillist.get_by_id(mail_id)
            await self.uow.commit()
            return mail
    
    async def get_emails_without_pagination(self) -> list[MailListSchema]:
        async with self.uow:
            all_mails = await self.uow.maillist.get_all_emails_without_pagination()
            await self.uow.commit()
            return all_mails
    
    async def update_email(self, mail_id: int, email_data: UpdateMailListSchema) -> MailListSchema:
        email_dict = email_data.model_dump()
        async with self.uow:
            updated_mail = await self.uow.maillist.update(mail_id, email_dict)
            await self.uow.commit()

            return updated_mail
    
    async def delete_email(self, mail_id: int) -> MailListSchema:
        async with self.uow:
            deleted_mail = await self.uow.maillist.delete(mail_id)
            await self.uow.commit()
            return deleted_mail