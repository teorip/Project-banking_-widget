import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


# Этот тест проверяет, что функция `filter_by_currency` корректно фильтрует транзакции
# по заданной валюте. Он создает список транзакций, вызывает функцию `filter_by_currency`
# с этой валютой и проверяет, что количество транзакций в результате равно ожидаемому
# количеству и что все транзакции имеют валюту, соответствующую параметру теста.
@pytest.mark.parametrize("currency, expected_count", [("USD", 3), ("RUB", 2)])
def test_filter_by_currency(by_currency, currency, expected_count):
    filtered_transactions = filter_by_currency(by_currency, currency)
    filtered_transactions_list = list(filtered_transactions)

    assert len(filtered_transactions_list) == expected_count
    for transaction in filtered_transactions_list:
        assert transaction["operationAmount"]["currency"]["code"] == currency


# Тест - проверка, что функция `filter_by_currency` выбрасывает исключение,
# если в списке транзакций нет транзакций с заданной валютой
def test_filter_by_currency_empty(empty_by_currency):
    with pytest.raises(ValueError, match="Транзакции в заданной валюте отсутствуют"):
        filter_by_currency(empty_by_currency, "EUR")


# Тест - функция возвращает корректные описания для каждой транзакции.
# Работа функции с различным количеством входных транзакций.
@pytest.mark.parametrize(
    "expected_descriptions",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(by_currency, expected_descriptions):
    descriptions = transaction_descriptions(by_currency)
    for expected_description in expected_descriptions:
        assert next(descriptions) == expected_description


# Тест - проверка, что функция `transaction_descriptions
# выбрасывает исключение, если принимает пустой список
def test_transaction_descriptions_empty(empty_by_currency):
    description = transaction_descriptions(empty_by_currency)
    with pytest.raises(ValueError, match="Введены пустые транзакции"):
        transaction_descriptions(empty_by_currency)
        assert next(description) == description


# Тест - проверка генератора карт
@pytest.mark.parametrize(
    "start, end, expected_card_numbers",
    [
        (
            1234432199995555,
            1234432199995560,
            [
                "1234 4321 9999 5555",
                "1234 4321 9999 5556",
                "1234 4321 9999 5557",
                "1234 4321 9999 5558",
                "1234 4321 9999 5559",
                "1234 4321 9999 5560",
            ],
        )
    ],
)
def test_card_number_generator(start, end, expected_card_numbers):
    card_numbers = card_number_generator(start, end)
    for expected_card_number in expected_card_numbers:
        assert next(card_numbers) == expected_card_number


# Тест - проверка формата генератора карт
@pytest.mark.parametrize(
    "start, end, expected_card_format", [(1, 1, "0000 0000 0000 0001")]
)
def test_card_number_generator_format(start, end, expected_card_format):
    assert str(next(card_number_generator(start, end))) == expected_card_format


# Тест - проверка генератора карт, если диапазон больше 9999999999999999
@pytest.mark.parametrize("expected_number", [10000000000000000])
def test_card_number_generator_no_diapason(number_no_diapason, expected_number):
    card = card_number_generator(number_no_diapason, expected_number)
    with pytest.raises(
        ValueError,
        match="Заданный диапазон карты не может быть больше 9999999999999999",
    ):
        assert str(next(card)) == expected_number
