from repositories.base import BaseRepository
from datetime import datetime, timedelta
from jose import jwt
from security.jwthandler import JWTHandler




class UsersRepository(BaseRepository):
    ...
    # async def get_travelers_of_manager(self, manager_id: int):
    #     manager = await self.get_by_id(manager_id)

    #     travelers = [traveler.traveler[0].to_read_model() for traveler in manager.travelers]
    #     return travelers

        
    
        