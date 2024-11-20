import os
from typing import Any, Union

from src.operations_csv_xls import get_operations_csv, get_operations_xlsx
from src.processing import filter_by_state, sort_by_date
from src.transactions_word_description import transactions_word
from src.utils import financial_transactions


def number() -> list[dict]:
    """Функция выбора файла"""
    modul = [{}]
    while True:
        user = input(
            """Программа: Привет! Добро пожаловать в программу работы \nс банковскими транзакциями.
                Выберите необходимый пункт меню:
                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла\nПользователь: """
        ).lower()
        if user == "1":
            print("Программа: Для обработки выбран JSON-файл.")
            modul = financial_transactions("C:/Users/Admin/PycharmProjects/my_prj/Project_DZ_9.1/data/operations.json")
            break
        elif user == "2":
            print("Программа: Для обработки выбран CSV-файл.")
            modul = get_operations_csv(os.path.join(os.path.abspath(__file__), "../../data/transactions.csv"))
            break
        elif user == "3":
            print("Программа: Для обработки выбран XLSX-файл.")
            modul = get_operations_xlsx(os.path.join(os.path.abspath(__file__), "../../data/transactions_excel.xlsx"))
            break
        else:
            print("Программа: Такого варианта не предусмотренно, попробуйте выбрать еще раз.")
            continue
    return modul


def status(modul: list[dict]) -> list[dict]:
    """Функция выбора статуса"""
    a = 1
    while a > 0:
        user_2 = input(
            """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: """
        ).upper()
        if user_2.upper() == "EXECUTED":
            print("Программа: Операции отфильтрованы по статусу: EXECUTED")
            a -= 1
            modul_transaction = filter_by_state(modul, state="EXECUTED")
            return modul_transaction
        elif user_2.upper() == "CANCELED":
            print("Программа: Операции отфильтрованы по статусу: CANCELED")
            a -= 1
            modul_transaction = filter_by_state(modul, state="CANCELED")
            return modul_transaction
        elif user_2.upper() == "PENDING":
            print("Программа: Операции отфильтрованы по статусу: PENDING")
            a -= 1
            modul_transaction = filter_by_state(modul, state="PENDING")
            return modul_transaction
        else:
            print(f"Программа: Статус операции {user_2} недоступен")
            a += 1
            continue


def ad_questions(modul_transaction: list[dict]) -> Union[list[dict], Any]:
    """Функция, задающая дополнительные вопросы"""
    final = [{}]
    user_3 = input("Отсортировать операции по дате? Да/Нет \nПользователь: ").lower()
    user_4 = input("Отсортировать по возрастанию или по убыванию? \nПользователь: ").lower()
    user_5 = input("Выводить только рублевые транзакции? Да/Нет \nПользователь: ").lower()
    user_6 = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет \nПользователь: "
    ).lower()
    if user_3 == "да":
        if user_4 == "по возрастанию":
            sort_to_date = []
            sort = sort_by_date(modul_transaction, ascending="False")
            for i in sort:
                sort_to_date.append(i)
            if user_5 == "да":
                sort_to_rub = []
                for sort in sort_to_date:
                    if sort["operationAmount"]["currency"]["code"] == "RUB":
                        sort_to_rub.append(sort)
                if user_6 == "да":
                    user_7 = input("Выберите слово, по которому производится сортировка: ").lower()
                    final = transactions_word(sort_to_rub, user_7)
                    if not final or final == []:
                        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                elif user_6 == "нет":
                    final = sort_to_rub
            elif user_5 == "нет":
                sort_to_rub = sort_to_date
                if user_6 == "да":
                    user_7 = input("Выберите слово, по которому производится сортировка: ").lower()
                    final = transactions_word(sort_to_rub, user_7)
                    if not final or final == []:
                        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                elif user_6 == "нет":
                    final = sort_to_rub
        elif user_4 == "по убыванию":
            sort_to_date = []
            sort = sort_by_date(modul_transaction, ascending="True")
            for k in sort:
                sort_to_date.append(k)
            if user_5 == "да":
                sort_to_rub = []
                for sort in sort_to_date:
                    if sort["operationAmount"]["currency"]["code"] == "RUB":
                        sort_to_rub.append(sort)
                if user_6 == "да":
                    user_7 = input("Выберите слово, по которому производится сортировка: ").lower()
                    final = transactions_word(sort_to_rub, user_7)
                    if not final or final == []:
                        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                elif user_6 == "нет":
                    final = sort_to_rub
            elif user_5 == "нет":
                sort_to_rub = sort_to_date
                if user_6 == "да":
                    user_7 = input("Выберите слово, по которому производится сортировка: ").lower()
                    final = transactions_word(sort_to_rub, user_7)
                    if not final or final == []:
                        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
                elif user_6 == "нет":
                    final = sort_to_rub
    elif user_3 == "нет":
        if user_5 == "да":
            sort_to_rub = modul_transaction
            for sor in sort_to_rub:
                if sor["operationAmount"]["currency"]["code"] == "RUB":
                    sort_to_rub.append(sor)
            if user_6 == "да":
                user_7 = input("Выберите слово, по которому производится сортировка: ").lower()
                final = transactions_word(sort_to_rub, user_7)
                if not final or final == []:
                    return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
            elif user_6 == "нет":
                final = sort_to_rub
        elif user_5 == "нет":
            sort_to_rub = modul_transaction
            if user_6 == "да":
                user_7 = input("Выберите слово, по которому производится сортировка: ").lower()
                final = transactions_word(sort_to_rub, user_7)
                if not final or final == []:
                    return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
            elif user_6 == "нет":
                final = sort_to_rub
    return final
