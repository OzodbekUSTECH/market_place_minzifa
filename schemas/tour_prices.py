from schemas import CreateBaseModel, TourMixinBaseModel


class CreateTourPriceSchema(TourMixinBaseModel, CreateBaseModel):
    currency_id: int
    price: int | float
    discount_percentage: float | None = None
    new_price: float | None = None
    discount_start_date: str | None
    discount_end_date: str | None


class UpdateTourPriceSchema(CreateTourPriceSchema):
    pass


# class TourPriceSchema(CreateTourPriceSchema):
#     id: int


#     @validator('discount_percentage')
#     def round_discount(cls, value):
#         if value is not None:
#             return round(value)

#     @validator('new_price')
#     def round_new_price(cls, value):
#         if value is not None:
#             return round(value)
