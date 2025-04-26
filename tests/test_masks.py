import pytest

from src.masks import get_mask_account, get_mask_card_number

from typing import Union


@pytest.fixture
def card_number() -> int:
    return 7000792289606361


@pytest.mark.parametrize(
    "card_number, expected_result", [("3782822463100056", "3782 82** **** 0056")]
)
def test_get_mask_card_number(card_number: int, expected_result: str) -> None:
    assert get_mask_card_number(card_number) == expected_result


def test_get_mask_card_number_invalid_card_number(card_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("Invalid card number")


def test_get_mask_card_number_absent_card_number(card_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")


@pytest.fixture
def account() -> int:
    return 73654108430135874305


@pytest.mark.parametrize(
    "account, expected_result", [("11123456789012345600", "**5600")]
)
def test_get_mask_account(account: int, expected_result: str) -> None:
    assert get_mask_account(account) == expected_result


def test_get_mask_account_invalid_account(account: int) -> None:
    with pytest.raises(ValueError):
        get_mask_account("Invalid account")


def test_get_mask_account_absent_account_number(account: int) -> None:
    with pytest.raises(ValueError):
        get_mask_account("")
