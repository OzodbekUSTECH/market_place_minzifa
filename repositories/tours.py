from repositories import BaseRepository, Pagination
from fuzzywuzzy import fuzz, process

class ToursRepository(BaseRepository):
    async def get_list_of_tours_by_status_id(self, status_id: int, pagination: Pagination):
        tours = self.session.query(self.model).filter(self.model.status_id == status_id).offset(pagination.offset).limit(pagination.limit).all()
        self.session.commit()
        return tours
    
    async def search_tours_by_title(self, query: str, status_id: int):
        all_tours = await self.get_all()
        matched_tours = []

        for tour in all_tours:
        # Применение фильтров
            if (not status_id or tour.status_id == status_id):
                title_similarity = fuzz.partial_ratio(query.lower(), tour.title.lower())
                if title_similarity > 60:  # Минимальный порог сходства (можете настроить)
                    matched_tours.append(tour)

        return matched_tours


        
    

    