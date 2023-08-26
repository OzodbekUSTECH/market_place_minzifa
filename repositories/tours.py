from repositories import BaseRepository, Pagination

class ToursRepository(BaseRepository):
    async def get_list_of_tours_by_status_id(self, status_id: int, pagination: Pagination):
        tours = self.session.query(self.model).filter(self.model.status_id == status_id).offset(pagination.offset).limit(pagination.limit).all()
        self.session.commit()
        return tours
    

        
    

    