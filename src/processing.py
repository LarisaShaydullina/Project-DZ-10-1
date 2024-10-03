from typing import Any

dictionary_id = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

def filter_by_state(dictionary_id: list[dict[str, Any]], state: str = 'EXECUTED'):
    dictionary_executed = []
    for index in dictionary_id:
        if index['state'] == state:
            dictionary_executed.append(index)
    return dictionary_executed

print("Введите параметр для ключа состояния state (EXECUTED/CANCELED):")
state = input()
print(filter_by_state(dictionary_id, state))

def sort_by_date(dictionary_id: list[dict[str, Any]], ascending: bool = True):
    sorted_dictionary = sorted(dictionary_id, key = lambda dictionary_id: dictionary_id['date'], reverse = ascending)
    return sorted_dictionary

print(sort_by_date(dictionary_id))
