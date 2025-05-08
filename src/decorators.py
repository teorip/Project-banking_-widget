from functools import wraps


def log(filename=None):
    """Определение функции `log`,
    которая принимает один аргумент `filename` со значением по умолчанию `None`."""

    def log_decorator(func):
        """определение функции `log_decorator`, которая принимает один аргумент `func`.
        Эта функция будет использоваться для декорирования других функций."""

        @wraps(func)
        def wrapper(arg1, arg2):
            """Декоратор, который используется для сохранения метаданных функции `func`."""

            try:
                result = func(arg1, arg2)
                if filename:
                    with open(filename, "a") as f:
                        f.write("my_function ok\n")
                elif filename is None:
                    print(f"my_function ok. Inputs: {arg1}, {arg2}, Result: {result}")
                return result
            except ValueError as result:
                raise ValueError(
                    f"my_function error. Inputs: {arg1}, {arg2}, Result: {result}"
                )

        return wrapper

    return log_decorator
