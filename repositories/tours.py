from repositories import BaseRepository, Pagination
from fuzzywuzzy import fuzz, process

class ToursRepository(BaseRepository):
   
    
    async def search_tours(self, query: str, status_id: int, tour_rating: float, pagination: Pagination):
        all_tours = await self.get_all(pagination)
        matched_tours = []

        for tour in all_tours:
            # Применение фильтров
            if not status_id or tour.status_id == status_id:
                    
                if not query or fuzz.partial_ratio(query.lower(), tour.title.lower()) > 60:

                    if not tour_rating or tour.rating == tour_rating:

                        matched_tours.append(tour)

        print(matched_tours)
        return matched_tours








        
    

    