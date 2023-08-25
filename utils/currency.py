import requests
import httpx

class CurrencyHandler:

    @staticmethod
    async def get_exchange_rate(currency_name: str):
        upper_currency_name = currency_name.upper()
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.exchangerate-api.com/v4/latest/USD")
            data = response.json()
            exchange_rate = data['rates'][upper_currency_name]
            if exchange_rate:
                return float(exchange_rate)
            return None