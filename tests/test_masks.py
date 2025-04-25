import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number():
    return 7000792289606361


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number(123)


def test_get_mask_card_number_absent_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("")


def account():
    return 73654108430135874305


def test_get_mask_account():
    assert get_mask_account(account()) == "**4305"


def test_get_mask_account_invalid_account_number():
    with pytest.raises(ValueError):
        get_mask_account(123)


def test_get_mask_account_absent_account_number():
    with pytest.raises(ValueError):
        get_mask_account("")
