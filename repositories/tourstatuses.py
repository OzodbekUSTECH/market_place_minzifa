from repositories import BaseRepository
from schemas.tourstatuses import AllowedStatuses
from sqlalchemy import func
# func.lower(func.replace(self.model.name, " ", ""))
class TourStatusesRepository(BaseRepository):
    ...

    