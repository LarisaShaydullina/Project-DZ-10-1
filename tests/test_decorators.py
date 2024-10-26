from pathlib import Path
from typing import Any

from _pytest.capture import CaptureFixture

from src.decorators import my_function, log


def test_log_print_fail(tmp_path: Path) -> None:
    """Тестирование на запись в файл"""
    log_file = tmp_path / "test_output.txt"

    @log(log_file)
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function(1, 2)
    with open(log_file, "r") as f:
        expected_output = f.read()
    assert expected_output == "Function my_function started\nmy_function ok\nResult = 3\nFunction my_function finished"


def test_log_print_console(capsys: CaptureFixture[str]) -> None:
    """Тестирование на вывод в консоль"""
    my_function(1, 2)
    captured = capsys.readouterr()
    expected_output = "Function my_function started\nmy_function ok\nResult = 3\nFunction my_function finished\n"
    assert captured.out == expected_output


def test_log_print_fail_mistake(tmp_path: Path) -> None:
    """Тестирование на ошибку (если вместо числа ввели строковый тип/ запись в файл"""
    log_file = tmp_path / "test_output.txt"

    @log(log_file)
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function(1, "2")
    with open(log_file, "r") as f:
        expected_output = f.read()
    assert expected_output == (
        "Function my_function started\n"
        "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: ((1, '2'), {})\n"
        "Function my_function finished"
    )


def test_log_print_console_mistake(capsys: CaptureFixture[str]) -> None:
    """Тестирование на ошибку (если вместо числа ввели строковый тип/ вывод в консоль"""
    my_function(1, "2")
    captured = capsys.readouterr()
    expected_output = (
        "Function my_function started\n"
        "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: ((1, '2'), {})\n"
        "Function my_function finished\n"
    )
    assert captured.out == expected_output


def test_log(tmp_path: Path) -> None:
    """Тестирование на то, что функция выдает верный результат"""
    log_file = tmp_path / "test_output.txt"

    @log(log_file)
    def my_function(x: int, y: int) -> int:
        """Тест декоратора с записью в консоль на функции сложения двух чисел"""
        return x + y

    result = my_function(1, 2)
    assert result == 3
