from repositories import BaseRepository
from sqlalchemy import func


class TourActivitiesRepository(BaseRepository):
    
    async def get_list_of_activities_of_tour(self, tour_id: int):
        activities = self.session.query(self.model).filter(self.model.tour_id == tour_id).all()
        self.session.commit()
        return activities
        
        

        