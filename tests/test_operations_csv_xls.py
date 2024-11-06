import os
from typing import Any
from unittest.mock import patch
import pytest

from src.operations_csv_xls import get_operations_csv, get_operations_xlsx


@pytest.fixture
def test_transactions_csv_xlsx() -> list:
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]


PATH_1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "test_transactions.csv")
PATH_2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "test_transactions_excel.xlsx")


def test_get_operations_csv_none() -> None:
    """Тестирование функции, которая считывает финансовые операции из CSV-файла, если файл пустой"""
    assert get_operations_csv("[]") == []


@patch("src.operations_csv_xls.get_operations_csv")
def test_get_operations_csv(mock_read: Any, test_transactions_csv_xlsx: list) -> None:
    """Тестирование функции, которая считывает финансовые операции из CSV-файла"""
    mock_read.return_value = test_transactions_csv_xlsx
    assert get_operations_csv(PATH_1) == test_transactions_csv_xlsx


def test_get_operations_xlsx_none() -> None:
    """Тестирование функции, которая считывает финансовые операции из XLSX-файла, если файл пустой"""
    assert get_operations_xlsx("[]") == []


@patch("src.operations_csv_xls.get_operations_xlsx")
def test_get_operations_xlsx(mock_read: Any, test_transactions_csv_xlsx: list) -> None:
    """Тестирование функции, которая считывает финансовые операции из XLSX-файла"""
    mock_read.return_value = test_transactions_csv_xlsx
    assert get_operations_xlsx(PATH_2) == test_transactions_csv_xlsx
