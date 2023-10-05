from schemas.regions import CreateRegionSchema, UpdateRegionSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class RegionsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_region(self, region_data: CreateRegionSchema) -> models.Region:
        region_dict = region_data.model_dump()
        async with self.uow:
            region = await self.uow.regions.create(region_dict)
            await self.uow.commit()
            return region
        
    async def get_list_of_regions(self) -> list[models.Region]:
        async with self.uow:
            return await self.uow.regions.get_all()
        
    async def get_region_by_id(self, id: int) -> models.Region:
        async with self.uow:
            return await self.uow.regions.get_by_id(id)
        
    async def update_region(self, id: int, region_data: UpdateRegionSchema) -> models.Region:
        region_dict = region_data.model_dump()
        async with self.uow:
            region = await self.uow.regions.update(id, region_dict)
            await self.uow.commit()
            return region
        
    async def delete_region(self, id: int) -> models.Region:
        async with self.uow:
            region = await self.uow.regions.delete(id)
            await self.uow.commit()
            return region
        
regions_service = RegionsService()