from repositories.maillist import MailListRepository
from schemas.maillist import CreateMailListSchema, UpdateMailListSchema
from fastapi import HTTPException, status
from repositories.base import Pagination

class MailListService:
    def __init__(self, maillist_repo: MailListRepository):
        self.maillist_repo: MailListRepository = maillist_repo

    async def subscribe(self, mail_data: CreateMailListSchema):
        existing_email = await self.maillist_repo.get_by_email(mail_data.email)
        if existing_email:
            raise HTTPException(status_code=status.HTTP_200_OK, detail="You already subscribed!")
        mail_dict = mail_data.model_dump()
        return await self.maillist_repo.create(mail_dict)
    
    async def get_all_mails(self, pagination: Pagination):
        return await self.maillist_repo.get_all(pagination)
    
    async def get_mail_by_id(self, mail_id: int):
        return await self.maillist_repo.get_by_id(mail_id)
    
    async def get_emails_without_pagination(self):
        return await self.maillist_repo.get_all_emails_without_pagination()
    
    async def update_email(self, mail_id: int, email_data: UpdateMailListSchema):
        email_dict = email_data.model_dump()
        return await self.maillist_repo.update(mail_id, email_dict)
    
    async def delete_email(self, mail_id: int):
        return await self.maillist_repo.delete(mail_id)