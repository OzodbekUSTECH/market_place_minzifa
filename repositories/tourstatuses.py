from repositories import BaseRepository
from schemas.tourstatuses import AllowedStatuses
from sqlalchemy import func
# func.lower(func.replace(self.model.name, " ", ""))
class TourStatusesRepository(BaseRepository):
    async def get_id_of_published_status(self) -> int:
        published_status = self.session.query(self.model).filter(func.lower(func.replace(self.model.name, " ", "")) == AllowedStatuses.PUBLISHED.value.lower().replace(" ", "")).first()
        self.session.commit()
        return published_status.id
    
    async def get_id_of_archieved_status(self) -> int:
        published_status = self.session.query(self.model).filter(func.lower(func.replace(self.model.name, " ", "")) == AllowedStatuses.ARCHIVED.value.lower().replace(" ", "")).first()
        self.session.commit()
        return published_status.id
    

    