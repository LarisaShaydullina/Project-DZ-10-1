def get_mask_card_number(card_number: str) -> str:
    """
    Функция, которая принимает на вход Номер карты, и
    возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    mask_card_number = card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + card_number[-4:]
    return mask_card_number


def get_mask_account(account: str) -> str:
    """
    Функция, которая принимает на вход Номер счета, и
    возвращает маску номера по правилу **XXXX
    """
    mask_account = "**" + account[-4:]
    return mask_account
