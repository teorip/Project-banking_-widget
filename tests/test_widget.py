from typing import Any

import pytest

from src.widget import get_data, mask_account_card


# Тестирование функции get_data для проверки ее корректности
@pytest.mark.parametrize(
    "data, expected_result", [("2024-03-11T02:26:18.671407", "11.03.2024")]
)
def test_get_data(data: str, expected_result: str) -> None:
    assert get_data(data) == expected_result


# Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
# Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
def test_get_data_invalid_data(data_false: Any) -> None:
    with pytest.raises(ValueError, match="Неверный формат даты"):
        get_data(data_false)


# Тест для проверки, что функция корректно распознает и применяет нужный
# тип маскировки в зависимости от типа входных данных (карта или счет)
@pytest.mark.parametrize(
    "bank_details, expected_result",
    [("73654108430135874306", " **4306"), ("7365410843013587", " 7365 41** **** 3587")],
)
def test_mask_account_card(bank_details: int, expected_result: str) -> None:
    assert mask_account_card(bank_details) == expected_result


# Параметризованные тесты с разными типами карт
# и счетов для проверки универсальности функции.
@pytest.mark.parametrize(
    "bank_details, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7517252233333405", "MasterCard 7517 25** **** 3405"),
        ("Счет 47422845456939785778", "Счет **5778"),
    ],
)
def test_mask_account_card_universal(bank_details: int, expected_result: str) -> None:
    assert mask_account_card(bank_details) == expected_result


# Тестирование функции на обработку некорректных входных данных и
# проверка ее устойчивости к ошибкам.
def test_mask_account_card_invalid_input(bank_details_false: Any) -> None:
    with pytest.raises(ValueError, match="Введеные банковские данные не корректны"):
        mask_account_card(bank_details_false)
