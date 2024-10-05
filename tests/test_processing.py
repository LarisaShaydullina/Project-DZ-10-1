from src.processing import filter_by_state, sort_by_date

import pytest


def test_filter_by_state(filter_by_states_executed: str, filter_by_states_canceled: str, filter_by_states_no: str, filter_by_states_any: str) -> None:
    dictionary_fix = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(dictionary_fix, filter_by_states_executed) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert filter_by_state(dictionary_fix, filter_by_states_canceled) == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]
    assert filter_by_state(dictionary_fix, filter_by_states_no) == []
    assert filter_by_state(dictionary_fix, filter_by_states_any) == []


def test_sort_by_date(true_sort_by_date: list[dict[str, Any]], false_sort_by_date: list[dict[str, Any]]) -> None:
    dictionary_fix = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert sort_by_date(dictionary_fix, "True") == true_sort_by_date
    assert sort_by_date(dictionary_fix, "TRUE") == true_sort_by_date
    assert sort_by_date(dictionary_fix, "true") == true_sort_by_date
    assert sort_by_date(dictionary_fix, "False") == false_sort_by_date
    assert sort_by_date(dictionary_fix, "FALSE") == false_sort_by_date
    assert sort_by_date(dictionary_fix, "false") == false_sort_by_date


def test_sort_by_date(false_sort_by_no_date: str) -> None:
    dictionary_no_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "20181014T08:21:33.419441"},
]
    assert sort_by_date(dictionary_no_date, "True") == false_sort_by_no_date