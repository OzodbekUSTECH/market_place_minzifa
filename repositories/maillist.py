from repositories import BaseRepository
from schemas.maillist import MailListSchema

class MailListRepository(BaseRepository):
    
    async def get_all_emails_without_pagination(self) -> list[MailListSchema]:
        return self.session.query(self.model).all()
    
        