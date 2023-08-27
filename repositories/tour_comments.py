from repositories import BaseRepository, Pagination
from sqlalchemy import func


class TourCommentsRepository(BaseRepository):
    async def get_list_of_comments_of_tour(self, tour_id: int, pagination: Pagination):
        comments = self.session.query(self.model).order_by(self.model.id).filter(self.model.tour_id == tour_id).offset(pagination.offset).limit(pagination.limit).all()
        self.session.commit()
        return comments
        

        