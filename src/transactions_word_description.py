import re
from collections import Counter
from typing import Any


def transactions_word(transactions: list[dict], search_str: Any) -> list[dict]:
    """Функция поиска в строке по слову"""
    final_lst = []
    for transaction in transactions:
        final = re.findall(search_str.lower(), transaction.get("description").lower())
        if final:
            final_lst.append(transaction)
    return final_lst


# print(transactions_word([
#     {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#             "amount": "31957.58",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589"
#     },
#     {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {
#             "amount": "8221.37",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560"
#     },
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     },
#     {
#         "id": 587085106,
#         "state": "EXECUTED",
#         "date": "2018-03-23T10:45:06.972075",
#         "operationAmount": {
#             "amount": "48223.05",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Открытие вклада",
#         "to": "Счет 41421565395219882431"
#     }], "Перевод организации"))


def find_description(transactions: list[dict], descriptions: list) -> Any:
    """Функция выводящая словарь, в котором ключи - это описания операций,
    а значения - количество операций в словаре"""
    lst = []
    count = 0
    for transaction in transactions:
        for description in descriptions:
            if description == transaction["description"]:
                lst.append(transaction["description"])
    count = Counter(lst)
    return count
