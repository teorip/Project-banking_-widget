from functools import wraps


def log(filename=None):
    """Определение функции `log`,
    которая принимает один аргумент `filename` со значением по умолчанию `None`."""

    def log_decorator(func):
        """определение функции `log_decorator`, которая принимает один аргумент `func`.
        Эта функция будет использоваться для декорирования других функций."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            """Декоратор, который используется для сохранения метаданных функции `func`."""

            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as f:
                        f.write("my_function ok")
                elif not filename:
                    print(f"my_function ok. Inputs: {args}, {kwargs}, Result: {result}")
                return result
            except Exception as e:
                with open(filename, "a") as f:
                    f.write(
                        f"my_function error: {Exception} Inputs: {args}, {kwargs}, Result: {e}\n"
                    )

                raise Exception(e)

        return wrapper

    return log_decorator
