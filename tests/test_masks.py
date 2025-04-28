from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование правильности маскирования номера карты
@pytest.mark.parametrize(
    "card_number, expected_result", [("3782822463100056", "3782 82** **** 0056")]
)
def test_get_mask_card_number(card_number: int, expected_result: str) -> None:
    assert get_mask_card_number(card_number) == expected_result


# Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
# Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
def test_get_mask_card_number_invalid_card_number(card_number_false: Any) -> None:
    with pytest.raises(
        ValueError, match="Номер карты должен содержать только цифры и равен 16 цифрам"
    ):
        get_mask_card_number(card_number_false)


# Тестирование правильности маскирования номера счета
@pytest.mark.parametrize(
    "account, expected_result", [("11123456789012345600", "**5600")]
)
def test_get_mask_account(account: int, expected_result: str) -> None:
    assert get_mask_account(account) == expected_result


# Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.
def test_get_mask_account_invalid_account(account_len_false: int) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_len_false)


# Проверка работы функции с различными форматами и длинами номеров счетов
def test_get_mask_account_absent_account_number(account_format_false: Any) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_format_false)
