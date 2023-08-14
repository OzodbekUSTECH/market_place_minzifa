from repositories.base import BaseRepository
from datetime import datetime, timedelta
from jose import jwt
from security.jwthandler import JWTHandler




class UsersRepository(BaseRepository):
    async def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt =  await JWTHandler.encode(to_encode)
        return encoded_jwt

    async def get_travelers_of_manager(self, manager_id: int):
        manager = await self.get_by_id(manager_id)

        travelers = [traveler.traveler for traveler in manager.travelers]
        return travelers

        
    
        