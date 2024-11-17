import csv
import pandas as pd

from typing import Any, Collection


def get_operations_csv(file_csv: str) -> list[dict[str, dict[str, Collection[str]] | str]]:
    """Функция, которая считывает финансовые операции из CSV-файла"""
    transactions_csv = []
    try:
        with open(file_csv, encoding="utf-8") as file:
            reader_dicts = csv.DictReader(file, delimiter=";")
            for row in reader_dicts:
                transactions_csv.append(
                    {
                        "id": str(row["id"]),
                        "state": row["state"],
                        "date": row["date"],
                        "operationAmount": {
                            "amount": str(row["amount"]),
                            "currency": {
                                "name": row["currency_name"],
                                "code": row["currency_code"],
                            },
                        },
                        "description": row["description"],
                        "from": row["from"],
                        "to": row["to"],
                    }
                )
            return transactions_csv
    except FileNotFoundError:
        return []


def get_operations_xlsx(file_xlsx: str) -> list[dict[str, Any]]:
    """Функция, которая считывает финансовые операции из XLSX-файла"""
    transactions_xlsx = []
    try:
        transaction_xlsx = pd.read_excel(file_xlsx)
        for index, row in transaction_xlsx.iterrows():
            transactions_xlsx.append(
                {
                    "id": str(row["id"]),
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": str(row["amount"]),
                        "currency": {
                            "name": row["currency_name"],
                            "code": row["currency_code"],
                        },
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"],
                }
            )
        return transactions_xlsx
    except FileNotFoundError:
        return []


# print("Финансовые операции из CSV-файла")
# print(get_operations_csv("../data/transactions.csv"))
# print("Финансовые операции из XLSX-файла")
# print(get_operations_xlsx("../data/transactions_excel.xlsx"))
