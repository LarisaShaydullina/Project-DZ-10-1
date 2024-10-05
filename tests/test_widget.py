from src.widget import mask_account_card, get_date

import pytest

# номер карты может содержать от 16 до 20 цифр, номер счета может состоять только из 20 цифр
@pytest.mark.parametrize('user_type_and_number, mask_account_or_card', [
    ('Счет 42303978428284094137', 'Счет **4137'),
    ('счет 42303978428284094137', 'счет **4137'),
    ('СЧЕТ 42303978428284094137', 'СЧЕТ **4137'),
    ('СЧЕТ 4230397842828409413745454454', 'Некорректное значение номера счета'),
    ('Счет 42303', 'Некорректное значение номера счета'),
    ('Maestro 4213443989747112', 'Maestro 4213 44** **** 7112'),
    ('Visa 4213443989747112', 'Visa 4213 44** **** 7112'),
    ('UnionPay 42134439897471125', 'UnionPay 4213 44** **** 1125'),
    ('МИР 421344398974711255', 'МИР 4213 44** **** 1255'),
    ('AmericanExpress 4213443989747112555', 'AmericanExpress 4213 44** **** 2555'),
    ('Белкарт 42134439897471125555', 'Белкарт 4213 44** **** 5555'),
    ('Uzcard 4208125536456678777878454544', 'Некорректное значение номера счета, номера карты или типа платежной системы'),
    ('Мир 45544', 'Некорректное значение номера счета, номера карты или типа платежной системы'),
    ('fhjdshfdshks', 'Некорректное значение номера счета, номера карты или типа платежной системы'),
    ('проарпоаор 4523235688889569', 'Некорректное значение номера счета, номера карты или типа платежной системы'),
    ('Mastercard-4285963655693333', 'Mastercard 4285 96** **** 3333'),
    ('', 'Некорректное значение номера счета, номера карты или типа платежной системы')
])
def test_mask_account_card(user_type_and_number: str, mask_account_or_card: str) -> None:
    assert mask_account_card(user_type_and_number) == mask_account_or_card


def test_get_date(get_date_fix: str) -> None:
    assert get_date(get_date_fix) == '11.03.2024'

def test_get_date(get_date_no_fix: str) -> None:
    assert get_date(get_date_no_fix) == 'Некорректное значение'

def test_get_date(get_date_no_fix_t: str) -> None:
    assert get_date(get_date_no_fix_t) == 'Некорректное значение'

def test_get_date(get_date_no: str) -> None:
    assert get_date(get_date_no) == 'Некорректное значение'