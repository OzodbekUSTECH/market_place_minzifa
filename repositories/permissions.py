from repositories.base import BaseRepository




class PermissonsRepository(BaseRepository):
    async def get_by_endpoint(self, endpoint: str):
        instance = self.session.query(self.model).filter(self.model.endpoint == endpoint).first()

        return instance

    
    
        