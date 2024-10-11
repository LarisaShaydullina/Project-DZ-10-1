from functools import wraps
from typing import Any


def log(filename: Any) -> Any:
    """
    Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки
    """

    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: int, **kwargs: int) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"Function {func.__name__} started\n")
                        file.write(f"{func.__name__} ok\n")
                        file.write(f"Result = {result}\n")
                        file.write(f"Function {func.__name__} finished")
                else:
                    print(f"Function {func.__name__} started")
                    print(f"{func.__name__} ok")
                    print(f"Result = {result}")
                    print(f"Function {func.__name__} finished")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"Function {func.__name__} started\n")
                        file.write(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})\n")
                        file.write(f"Function {func.__name__} finished")
                else:
                    print(f"Function {func.__name__} started")
                    print(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})")
                    print(f"Function {func.__name__} finished")

        return wrapper

    return my_decorator


@log(filename="")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, "2")
