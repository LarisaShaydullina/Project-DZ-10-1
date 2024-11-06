import json
import logging
from json import JSONDecodeError
from typing import Any
from src.external_api import currency_conversion

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def financial_transactions(path_to_file: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях."""
    try:
        logger.info(f"Получение данных из файла {path_to_file}")
        print(f"Получение данных из файла {path_to_file}")
        with open(path_to_file, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                logger.error("Ошибка файла с транзакциями")
                print("Ошибка файла с транзакциями")
                return []
        if not isinstance(transactions, list):
            logger.error("Список транзакций пуст")
            print("Список транзакций пуст")
            return []
        logger.info("Список словарей с данными о финансовых транзакциях")
        print("Список словарей с данными о финансовых транзакциях")
        return transactions
    except FileNotFoundError:
        logger.error("Файл с транзакциями не найден")
        print("Файл с транзакциями не найден")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        logger.info("Код валюты в транзакции RUB")
        print("Код валюты в транзакции - RUB")
    else:
        amount = currency_conversion(trans)
        logger.info("Код валюты транзакции не RUB, произведена конвертация")
        print("Код валюты транзакции не RUB, произведена конвертация")
    return amount


print(financial_transactions("C:/Users/Admin/PycharmProjects/my_prj/Project_DZ_9.1/data/operations.json"))
print(
    transaction_amount(
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {"amount": "3348.98", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960",
        }
    )
)
