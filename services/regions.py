from schemas.regions import CreateRegionSchema, UpdateRegionSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
from repositories import paginate
import models

class RegionsService:
    

    async def create_region(self, uow: UnitOfWork, region_data: CreateRegionSchema) -> models.Region:
        region_dict = region_data.model_dump()
        async with uow:
            region = await uow.regions.create(region_dict)
            await uow.commit()
            return region
        
    async def get_list_of_regions(self, uow: UnitOfWork, country_id: int | None) -> list[models.Region]:
        async with uow:
            if country_id:
                return paginate(await uow.regions.get_all_by(country_id=country_id))
            return await uow.regions.get_all()
        
    async def get_region_by_id(self, uow: UnitOfWork, id: int) -> models.Region:
        async with uow:
            return await uow.regions.get_by_id(id)
        
    async def update_region(self, uow: UnitOfWork, id: int, region_data: UpdateRegionSchema) -> models.Region:
        region_dict = region_data.model_dump()
        async with uow:
            region = await uow.regions.update(id, region_dict)
            await uow.commit()
            return region
        
    async def delete_region(self, uow: UnitOfWork, id: int) -> models.Region:
        async with uow:
            region = await uow.regions.delete(id)
            await uow.commit()
            return region
        
regions_service = RegionsService()