from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_score: str) -> str:
    """
    Функция, которая возвращает строку с замаскированным номером карты или счета
    """
    if "Счет" in card_or_score:
        number_of_account = ""
        type_of_account = ""
        for index_account in card_or_score:
            if index_account.isdigit():
                number_of_account += index_account
            else:
                type_of_account += index_account
        return f"{type_of_account}{get_mask_account(number_of_account)}"
    else:
        number_of_card = ""
        type_of_card = ""
        for index_card in card_or_score:
            if index_card.isdigit():
                number_of_card += index_card
            else:
                type_of_card += index_card
        return f"{type_of_card}{get_mask_card_number(number_of_card)}"


def get_date(date: str) -> str:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"а
    """
    date = date.split("T")[0]
    year, month, day = date.split("-")
    correct_date = f"{day}.{month}.{year}"
    return correct_date
