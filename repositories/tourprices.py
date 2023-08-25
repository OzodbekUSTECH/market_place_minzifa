from repositories import BaseRepository

class TourPricesRepository(BaseRepository):
    async def get_by_tour_id(self, tour_id):
        return self.session.query(self.model).filter(self.model.tour_id == tour_id).all()
        
    

    