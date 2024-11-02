import os
import requests
from typing import Any
from dotenv import load_dotenv

load_dotenv()
values = os.getenv("API-KEY")


def currency_conversion(transaction: Any) -> Any:
    """Функция конвертации"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    response = requests.request("GET", url, headers={"apikey": values})
    result = response.json()
    return result["result"]
