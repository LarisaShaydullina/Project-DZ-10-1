from typing import Any

from src.transactions_word_description import find_description, transactions_word


def test_transaction_search_1(trial: list[dict], search_str: str, search_result: list[dict]) -> None:
    assert transactions_word(trial, search_str) == search_result


def test_find_description_1(trial: list[dict], description: list, counter_result: Any) -> None:
    assert find_description(trial, description) == counter_result
