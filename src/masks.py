def get_mask_card_number(card_number: str) -> str:
    """
    Функция, которая принимает на вход Номер карты, и
    возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    if 16 <= len(card_number) <= 20 and card_number.isdigit():
        mask_card_number = card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + ' ' + card_number[-4:]
        return mask_card_number
    else:
        return 'Некорректное значение номера карты'


def get_mask_account(account: str) -> str:
    """
    Функция, которая принимает на вход Номер счета, и
    возвращает маску номера по правилу **XXXX
    """
    if len(account) == 20:
        mask_account = "**" + account[-4:]
        return mask_account
    else:
        return 'Некорректное значение номера счета'
