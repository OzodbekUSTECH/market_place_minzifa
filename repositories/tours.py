from repositories import BaseRepository, Pagination
from fuzzywuzzy import fuzz, process

class ToursRepository(BaseRepository):
    async def get_list_of_tours_by_status_id(self, status_id: int, pagination: Pagination):
        tours = self.session.query(self.model).filter(self.model.status_id == status_id).offset(pagination.offset).limit(pagination.limit).all()
        self.session.commit()
        return tours
    
    async def search_tours_by_title(self, query: str):
        all_tours = await self.get_all()
        if not query:
            return all_tours
        tour_titles = [tour.title for tour in all_tours]
        results = process.extract(query, tour_titles, scorer=fuzz.token_set_ratio)
        matched_tours = []

        for result in results:
            if result[1] > 60:  # Минимальный порог схожести (можете настроить)
                matched_tour = all_tours[tour_titles.index(result[0])]
                matched_tours.append(matched_tour)

        return matched_tours


        
    

    