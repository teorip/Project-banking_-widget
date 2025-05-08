import pytest

from src.decorators import log


def test_log_the_parameter():
    @log(filename="mylog.txt")
    def my_function1(arg1, arg2, depth=0):
        if depth > 1:
            my_function1(arg1, arg2, depth - 1)


def test_my_function(capsys):
    @log()
    def my_function2(arg1, arg2):
        return arg1 + arg2

    my_function2(arg1=1, arg2=2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok. Inputs: 1, 2, Result: 3\n"


@log()
def my_function3(arg1, arg2):
    raise ValueError(f"my_function error. Inputs: {arg1}, {arg2}")


def test_log():
    with pytest.raises(Exception, match="my_function error. Inputs: 1, 2"):
        my_function3(arg1=1, arg2=2)
