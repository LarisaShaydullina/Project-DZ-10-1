import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция, которая принимает на вход Номер карты, и
    возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    if 16 <= len(card_number) <= 20 and card_number.isdigit():
        logger.info(f"Введенный номер карты: {card_number}, содержит от 16 до 20 цифр")
        mask_card_number = card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]
        logger.info(f"Замаскированный номер карты: {mask_card_number}")
        return mask_card_number
    else:
        logger.error("Произошла ошибка: некорректное значение номера карты")
        return "Некорректное значение номера карты"


def get_mask_account(account: str) -> str:
    """
    Функция, которая принимает на вход Номер счета, и
    возвращает маску номера по правилу **XXXX
    """
    if len(account) == 20:
        logger.info(f"Введенный номер счета: {account}, содержит 20 цифр")
        mask_account = "**" + account[-4:]
        logger.info(f"Замаскированный номер счета: {mask_account}")
        return mask_account
    else:
        logger.error("Произошла ошибка: некорректное значение номера счета")
        return "Некорректное значение номера счета"


if __name__ == "__main__":
    mask_card_result = get_mask_card_number("1111222233334444")
    mask_account_result = get_mask_account("12345678910111213141")
    print(f"Маска карты: {mask_card_result} \nМаска счета: {mask_account_result}")
