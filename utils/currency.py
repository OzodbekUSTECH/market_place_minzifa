import requests
import httpx

class CurrencyHandler:

    @staticmethod
    def get_exchange_rate(currency_name: str):
        upper_currency_name = currency_name.upper()
        url = f"https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['rates'][upper_currency_name]
        if exchange_rate:
            return float(exchange_rate)
        return None