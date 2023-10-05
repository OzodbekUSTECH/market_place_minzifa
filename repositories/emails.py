from repositories import BaseRepository
from sqlalchemy import insert, select, update, delete, desc

class EmailsRepository(BaseRepository):
    

    async def get_all_emails_by_language(self, language: str, reverse: bool = False):
        stmt = select(self.model).where(self.model.language == language)

        if reverse:
            stmt = stmt.order_by(desc(self.model.id))
        else:
            stmt = stmt.order_by(self.model.id)
            
        result = await self.session.execute(stmt)

        return result.scalars().all()
