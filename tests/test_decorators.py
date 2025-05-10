import pytest

from src.decorators import log


def test_log_the_parameter():
    @log(filename="mylog.log")
    def my_function1(a, b):
        return a + b

    my_function1(1, 2)
    with open("mylog.log", "r") as f:
        log_content = f.read()
        assert "my_function ok" in log_content


def test_my_function(capsys):
    @log()
    def my_function2(a, b):
        return a + b

    my_function2(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok. Inputs: (1, 2), {}, Result: 3\n"


@log(filename="mylog.log")
def my_function3(a, b):
    raise Exception("ZeroDivisionError: division by zero")


def test_log():
    with pytest.raises(Exception, match="ZeroDivisionError: division by zero"):
        my_function3(2, 0)


def test_log_file():
    @log(filename="mylog.log")
    def my_function4(a, b):
        pass

    with open("mylog.log", "r") as f:
        log_content = f.read()
        assert (
            "my_function error: <class 'Exception'> Inputs: (2, 0), {}, Result: ZeroDivisionError: division by zero"
            in log_content
        )
