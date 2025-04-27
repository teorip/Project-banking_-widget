from typing import Union

import pytest

from src.widget import get_data, mask_account_card


@pytest.fixture
def data() -> str|int:
    return format("%Y-%m-%dT%H:%M:%S.%f")


@pytest.mark.parametrize(
    "data, expected_result", [("2024-03-11T02:26:18.671407", "11.03.2024")]
)
def test_get_data(data: str, expected_result: str) -> None:
    assert get_data(data) == expected_result


def test_get_data_invalid_data(data: str|int) -> None:
    with pytest.raises(ValueError):
        result = "invalid_data"
        get_data (result)


def test_get_data_absent_of_date(data: str) -> None:
    with pytest.raises(ValueError):
        get_data("")


@pytest.fixture
def bank_details() -> int:
    return 73654108430135874306


@pytest.mark.parametrize(
    "bank_details, expected_result",
    [("73654108430135874306", " **4306"), ("7365410843013587", " 7365 41** **** 3587")],
)
def test_mask_account_card(bank_details: int, expected_result: str) -> None:
    assert mask_account_card(bank_details) == expected_result


@pytest.mark.parametrize(
    "bank_details, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7517252233333405", "MasterCard 7517 25** **** 3405"),
        ("Счет 47422845456939785778", "Счет **5778"),
    ],
)
def test_mask_account_card(bank_details: Union[str, int], expected_result: str):
    assert mask_account_card(bank_details) == expected_result


def test_mask_account_card_invalid_input(bank_details: int) -> None:
    with pytest.raises(ValueError):
        mask_account_card("invalid_input")


def test_mask_account_card_absent_input(bank_details: int) -> None:
    with pytest.raises(ValueError):
        mask_account_card("")
