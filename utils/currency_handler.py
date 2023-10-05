import requests
import httpx

class CurrencyHandler:

    @staticmethod
    async def get_exchange_rate(base_currency: str, target_currency_name: str) -> float | None:
        upper_base_currency_name = base_currency["en"].upper()
        upper_target_currency_name = target_currency_name["en"].upper()
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.exchangerate-api.com/v4/latest/{upper_base_currency_name}")
            data = response.json()
            exchange_rate = data['rates'][upper_target_currency_name]
            if exchange_rate:
                return exchange_rate
            return None