import os
from typing import Any
from unittest.mock import patch

import pytest

from src.utils import financial_transactions, transaction_amount


@pytest.fixture
def path() -> str:
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


@pytest.fixture
def path_empty_list() -> str:
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "[]")
    return PATH_TO_FILE


@pytest.fixture
def path_mistake_json() -> str:
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_1.json")
    return PATH_TO_FILE


@pytest.fixture
def trans() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def trans_1() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_financial_transactions_no_file() -> None:
    assert financial_transactions("no_file") == []


def test_financial_transactions(path: str) -> None:
    assert financial_transactions(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_financial_transactions_empty_list(path_empty_list: str) -> None:
    assert financial_transactions(path_empty_list) == []


def test_financial_transactions_mistake_json(path_mistake_json: str) -> None:
    assert financial_transactions(path_mistake_json) == []


def test_transaction_amount(trans: dict) -> None:
    assert transaction_amount(trans) == "31957.58"


@patch("src.utils.currency_conversion")
def test_transaction_amount_non_rub(mock_currency_conversion: Any, trans_1: dict) -> None:
    mock_currency_conversion.return_value = 1000.0
    assert transaction_amount(trans_1) == 1000.0
