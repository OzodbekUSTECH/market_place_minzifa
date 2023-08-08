from repositories.base import BaseRepository



class MailListRepository(BaseRepository):
    
    async def get_all_emails_without_pagination(self):
        return self.session.query(self.model).all()
    
        