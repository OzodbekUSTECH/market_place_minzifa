from models import Currency
from schemas.tour_prices import CreateTourPriceSchema, UpdateTourPriceSchema
from typing import Union
from utils.exceptions import CustomExceptions
from utils.currency_handler import CurrencyHandler

class TourPriceHandler:

    @staticmethod
    async def create_price_dict(
        target_currency: Currency,
        base_currency: Currency,
        price_data: Union[CreateTourPriceSchema, UpdateTourPriceSchema]
    ) -> dict:
        if target_currency == base_currency:
            converted_price = price_data.price
        else:
            exchange_rate = await CurrencyHandler.get_exchange_rate(base_currency.name, target_currency.name)
            if exchange_rate:
                converted_price = price_data.price * exchange_rate
            else:
                converted_price = price_data.price * target_currency.exchange_rate

        discount_percentage = None  # Изменил инициализацию на None
        converted_new_price = None  # Изменил инициализацию на None

        if price_data.new_price is not None and price_data.discount_percentage is not None:
            raise CustomExceptions.conflict("You can only fill either the new price or the discount")
        if price_data.discount_percentage:
            converted_new_price = await TourPriceHandler._calculate_new_price(converted_price, price_data.discount_percentage)
            discount_percentage = price_data.discount_percentage

        elif price_data.new_price:
            if target_currency == base_currency:
                discount_percentage = await TourPriceHandler._calculate_discount(converted_price, price_data.new_price)
                converted_new_price = price_data.new_price
            else:
                exchange_rate = await CurrencyHandler.get_exchange_rate(base_currency.name, target_currency.name)
                converted_new_price = price_data.new_price * exchange_rate
                discount_percentage = await TourPriceHandler._calculate_discount(converted_price, converted_new_price)

        price_dict = CreateTourPriceSchema(
                tour_id= price_data.tour_id,
                currency_id= target_currency.id,
                price= converted_price,
                discount_percentage= discount_percentage,
                new_price= converted_new_price,
                discount_start_date=price_data.discount_start_date,
                discount_end_date=price_data.discount_end_date
            ).model_dump()

        return price_dict
    
    @staticmethod
    async def _calculate_discount(previous_price: int, new_price: int) -> float:
            discount_percentage = ((previous_price - new_price) / previous_price) * 100
            return discount_percentage

    @staticmethod
    async def _calculate_new_price(previous_price: int, discount_percentage: int) -> float:
            new_price = previous_price - (previous_price * discount_percentage / 100)
            return new_price