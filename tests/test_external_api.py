from typing import Any
from unittest.mock import patch
import pytest
from src.external_api import currency_conversion


@pytest.fixture
def trans_1() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "3348.98", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@patch("src.external_api.requests.request")
def test_currency_conversion(mock_get: Any, trans_1: dict) -> None:
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 3348.98},
        "info": {"timestamp": 1730236442, "rate": 97.5034},
        "date": "2024-10-29",
        "result": 325603.090204,
    }
    assert currency_conversion(trans_1) == 325603.090204
