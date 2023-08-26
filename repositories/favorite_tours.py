from repositories import BaseRepository, Pagination



class FavoriteToursRepository(BaseRepository):    
    async def get_list_of_favorite_tours_of_user(self, user_id: int, pagination: Pagination):
        favorite_tours = self.session.query(self.model).filter(self.model.user_id == user_id).offset(pagination.offset).limit(pagination.limit).all()
        self.session.commit()
        return favorite_tours
    
    