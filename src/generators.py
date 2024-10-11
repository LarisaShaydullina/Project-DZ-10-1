import sys
from typing import Any, Generator


def filter_by_currency(transactions: Any, user_currency: str = "USD") -> Generator[Any, Any, None]:
    """
    Функция, принимающая на вход список словарей, представляющих транзакции -
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    """
    if transactions == []:
        sys.exit("Нет транзакций")
    if user_currency != "USD" and user_currency != "RUB":
        sys.exit("Транзакций в такой валюте нет")
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == user_currency:
            yield i


def transaction_descriptions(transactions: Any) -> Generator[Any, Any, None]:
    """
    Генератор, принимающий список словарей с транзакциями -
    возвращает описание каждой операции по очереди
    """
    if transactions == []:
        sys.exit("Нет транзакций")
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[Any, Any, None]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где Х — цифра номера карты. Генератор может сгенерировать номера карт в заданном
    диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    for number in range(start, stop + 1):
        # card_number = str(random.randint(1,9999999999999999))
        # if len(card_number) == 16:
        #     formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}
        card_number = f"{number:0>16}"
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number
