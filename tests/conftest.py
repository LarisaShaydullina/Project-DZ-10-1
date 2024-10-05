import pytest
from typing import Any

dictionary_id = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.fixture
def get_date_fix() -> str:
    return ('2024-03-11T02:26:18.671407')


@pytest.fixture
def get_date_no_fix() -> str:
    return ('20240311T02:26:18.671407')


@pytest.fixture
def get_date_no_fix_t() -> str:
    return ('2024-03-11M02:26:18.671407')


@pytest.fixture
def get_date_no() -> str:
    return ('')


@pytest.fixture
def filter_by_states_executed() -> str:
    return "EXECUTED"


@pytest.fixture
def filter_by_states_canceled() -> str:
    return "CANCELED"


@pytest.fixture
def filter_by_states_no() -> str:
    return ""


@pytest.fixture
def filter_by_states_any() -> str:
    return "Привет"


@pytest.fixture
def true_sort_by_date() -> list[dict[str, Any]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def false_sort_by_date() -> list[dict[str, Any]]:
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


@pytest.fixture
def false_sort_by_no_date() -> str:
    return "Некорректное значение даты"
