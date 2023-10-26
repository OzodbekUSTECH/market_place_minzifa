from schemas.tours_package.includes import (
    CreateMultipleIncludeInPrice,
    CreateIncludeInPriceSchema,
    UpdateIncludeInPriceSchema,
)
from database import UnitOfWork
import models
class IncludesInPriceService:
    
    async def create_multiple_includes_in_price(
            self, 
            uow: UnitOfWork,
            tour_id: int, 
            includes_data: list[CreateMultipleIncludeInPrice]) -> None:
        async with uow:
            tour: models.Tour = await uow.tours.get_by_id(tour_id)
            await uow.tour_includes.bulk_create(
                data_list=[CreateIncludeInPriceSchema(
                    tour_id=tour.id,
                    name=data.name,
                ).model_dump() for data in includes_data]
            )
            await uow.commit()

    async def create_include_in_price(self, uow: UnitOfWork, include_data: CreateIncludeInPriceSchema) -> models.IncludeInPrice:
        async with uow:
            include_in_price = await uow.tour_includes.create(include_data.model_dump())
            await uow.commit()
            return include_in_price
        
    async def get_includes_in_price_of_tour(self, uow: UnitOfWork, tour_id: int) -> list[models.IncludeInPrice]:
        async with uow:
            return await uow.tour_includes.get_all_by(tour_id=tour_id)
        
    async def update_include_in_price(self, uow: UnitOfWork, id: int, include_data: UpdateIncludeInPriceSchema) -> models.IncludeInPrice:
        async with uow:
            include_in_price: models.IncludeInPrice = await uow.tour_includes.get_by_id(id)
            await uow.tour_includes.update(include_in_price.id, include_data.model_dump())
            await uow.commit()
            return include_in_price
        
    async def delete_include_in_price(self, uow: UnitOfWork, id: int) -> models.IncludeInPrice:
        async with uow:
            include_in_pirce: models.IncludeInPrice = await uow.tour_includes.get_by_id(id)
            await uow.tour_includes.delete(include_in_pirce.id)
            await uow.commit()
            return include_in_pirce
        
tour_includes_service = IncludesInPriceService()
            