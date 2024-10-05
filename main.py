from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

dictionary_id = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

number = ""
print("Введите тип и номер карты или введите счет:")
user_card_or_score = input()
print(mask_account_card(user_card_or_score))

print("Введите дату:")
user_date = input()
print(get_date(user_date))

print("Введите параметр для ключа состояния операций state, успешные или отмененные (EXECUTED/CANCELED):")
state = input()
print(filter_by_state(dictionary_id, state))

print("Введите метод сортировки операций, по убыванию или по возрастанию (True/False):")
ascending = input()
print(sort_by_date(dictionary_id, ascending))
