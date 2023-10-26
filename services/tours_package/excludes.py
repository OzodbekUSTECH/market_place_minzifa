from schemas.tours_package.excludes import (
    CreateMultipleExcludeInPrice,
    CreateExcludeInPriceSchema,
    UpdateExcludeInPriceSchema,
)
from database import UnitOfWork
import models
class ExcludesInPriceService:

    async def create_multiple_excludes_in_price(
            self, 
            uow: UnitOfWork,
            tour_id: int, 
            excludes_data: list[CreateMultipleExcludeInPrice]
        ) -> None:
        async with uow:
            tour: models.Tour = await uow.tours.get_by_id(tour_id)
            await uow.tour_excludes.bulk_create(
                data_list=[CreateExcludeInPriceSchema(
                    tour_id=tour.id,
                    name=data.name,
                ).model_dump() for data in excludes_data]
            )
            await uow.commit()

    async def create_exclude_in_price(self, uow: UnitOfWork, exclude_data: CreateExcludeInPriceSchema) -> models.IncludeInPrice:
        async with uow:
            exclude_in_price = await uow.tour_excludes.create(exclude_data.model_dump())
            await uow.commit()
            return exclude_in_price
        
    async def get_excludes_in_price_of_tour(self, uow: UnitOfWork, tour_id: int) -> list[models.ExcludeInPrice]:
        async with uow:
            return await uow.tour_excludes.get_all_by(tour_id=tour_id)
        
    async def update_exclude_in_price(self, uow: UnitOfWork, id: int, exclude_data: UpdateExcludeInPriceSchema) -> models.IncludeInPrice:
        async with uow:
            exclude_in_price: models.IncludeInPrice = await uow.tour_excludes.get_by_id(id)
            await uow.tour_excludes.update(exclude_in_price.id, exclude_data.model_dump())
            await uow.commit()
            return exclude_in_price
        
    async def delete_exclude_in_price(self, uow: UnitOfWork, id: int) -> models.IncludeInPrice:
        async with uow:
            exclude_in_price: models.IncludeInPrice = await uow.tour_excludes.get_by_id(id)
            await uow.tour_excludes.delete(exclude_in_price.id)
            await uow.commit()
            return exclude_in_price
        
tour_excludes_service = ExcludesInPriceService()
            