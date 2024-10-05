from typing import Any

from src.widget import get_date


def filter_by_state(dictionary_id: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Функция, которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению (по умолчанию 'EXECUTED')
    """
    dictionary_executed = []
    for index in dictionary_id:
        if index["state"] == state.upper():
            dictionary_executed.append(index)
    return dictionary_executed



def sort_by_date(dictionary_id: list[dict[str, Any]], ascending: str = 'True') -> list[dict[str, Any]]:
    """
    Функция, которая возвращает новый список, отсортированный по убыванию/возрастанию по дате(date)
    """
    for index in dictionary_id:
        if get_date(index["date"]) == 'Некорректное значение':
            return 'Некорректное значение даты'
    if ascending.title() == 'True':
        sorted_dictionary = sorted(dictionary_id, key=lambda dictionary_id: dictionary_id["date"], reverse = ascending)
    elif ascending.title() == 'False':
        sorted_dictionary = sorted(dictionary_id, key=lambda dictionary_id: dictionary_id["date"], reverse = False)
    else:
        return 'Некорректное значение метода сортировки'
    return sorted_dictionary
