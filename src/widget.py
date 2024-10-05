from src.masks import get_mask_card_number, get_mask_account

cards_payment_system = [
    'Visa', 'Mastercard', 'Maestro', 'МИР', 'UnionPay', 'AmericanExpress',
    'Discover', 'RuPay', 'Uzcard', 'Humo', 'Shetab', 'ArmenianCard',
    'BankNet', 'Troy', 'Белкарт'
]

def mask_account_card(card_or_score: str) -> str:
    """
    Функция, которая возвращает строку с замаскированным номером карты или счета
    """
    if "Счет" in card_or_score or 'счет' in card_or_score or 'СЧЕТ' in card_or_score:
        number_of_account = ""
        type_of_account = ""
        for index_account in card_or_score:
            if index_account.isdigit():
                number_of_account += index_account
            elif index_account.isalpha():
                type_of_account += index_account
        if (get_mask_account(number_of_account) != "Некорректное значение номера счета"):
            return f"{type_of_account} {get_mask_account(number_of_account)}"
        else:
            return get_mask_account(number_of_account)
    else:
        number_of_card = ""
        type_of_card = ""
        count = 0
        for index_card in card_or_score:
            if index_card.isdigit():
                number_of_card += index_card
            elif index_card.isalpha():
                type_of_card += index_card
        for i in cards_payment_system:
            if type_of_card == i:
                count = 1
        if (get_mask_card_number(number_of_card) != "Некорректное значение номера карты") and (count == 1):
            return f"{type_of_card} {get_mask_card_number(number_of_card)}"
        else:
            return 'Некорректное значение номера счета, номера карты или типа платежной системы'



def get_date(date: str) -> str:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"а
    """
    if len(date) == 26 and date[10] == 'T' and date[4] == '-' and date[7] == '-':
        date = date.split("T")[0]
        year, month, day = date.split("-")
        correct_date = f"{day}.{month}.{year}"
        return correct_date
    else:
        return ('Некорректное значение')
