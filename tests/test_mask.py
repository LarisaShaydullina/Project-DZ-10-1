from src.masks import get_mask_card_number, get_mask_account

import pytest


# номер карты может содержать от 16 до 20 цифр
@pytest.mark.parametrize(
    "number, mask_card",
    [
        ("4196556658925893", "4196 55** **** 5893"),
        ("4111216789888682", "4111 21** **** 8682"),
        ("42134439897471125", "4213 44** **** 1125"),
        ("421344398974711215", "4213 44** **** 1215"),
        ("4213443989747112155", "4213 44** **** 2155"),
        ("42134439897471121555", "4213 44** **** 1555"),
        ("4208125536456678777878454544", "Некорректное значение номера карты"),
        ("4255", "Некорректное значение номера карты"),
        ("fhjdshfdshks", "Некорректное значение номера карты"),
        ("проарпоаор", "Некорректное значение номера карты"),
        ("GHGhаорвооОР/воу=арfh", "Некорректное значение номера карты"),
        ("", "Некорректное значение номера карты"),
    ],
)
def test_get_mask_card_number(number: str, mask_card: str) -> None:
    assert get_mask_card_number(number) == mask_card


# Номер счета может состоять только из 20 цифр
@pytest.mark.parametrize(
    "account, mask_account",
    [
        ("42303978428284094137", "**4137"),
        ("40703978173422706025", "**6025"),
        ("42002810136874925344454544", "Некорректное значение номера счета"),
        ("408028", "Некорректное значение номера счета"),
        ("ghjhkdshk", "Некорректное значение номера счета"),
        ("праовпр", "Некорректное значение номера счета"),
        ("праов5656RTRYTrtsvdvbпр", "Некорректное значение номера счета"),
        ("", "Некорректное значение номера счета"),
    ],
)
def test_get_mask_account(account: str, mask_account: str) -> None:
    assert get_mask_account(account) == mask_account
