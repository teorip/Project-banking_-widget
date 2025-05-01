from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Тестирование фильтрации списка словарей по заданному статусу state
@pytest.mark.parametrize(
    "lis_date, state, expected_result",
    [
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            "EXECUTED",
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ],
        )
    ],
)
def tests_filter_by_state(
    lis_date: List[Dict[str, Any]], state: str, expected_result: List[Dict[str, Any]]
) -> None:
    assert filter_by_state(lis_date, state) == expected_result


# Проверка, что функция выбрасывает исключение при отсутствии словарей с указанным статусом
def test_filter_by_state_no_matching_state(
    list_no_executed: List[Dict[str, Any]],
) -> None:
    with pytest.raises(
        ValueError, match="Отсутствуют словари с указанным статусом в списке"
    ):
        filter_by_state(list_no_executed, state="EXECUTED")


# Параметризация тестов для различных возможных значений статуса state
@pytest.mark.parametrize("state", ["EXECUTED", "CANCELED"])
def tests_filter_by_state_different_state(
    list_executed: List[Dict[str, Any]], state: str
) -> None:
    result = filter_by_state(list_executed, state)
    assert all(item["state"] == state for item in result)


# Тестирование сортировки списка словарей по датам в порядке убывания
@pytest.mark.parametrize(
    "expected_result",
    [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
        ]
    ],
)
def test_sort_by_date_rev_true(
    list_executed: List[Dict[str, Any]], expected_result: List[Dict[str, Any]]
) -> None:
    assert sort_by_date(list_executed, reverse=True) == expected_result


# Тестирование сортировки списка словарей по датам в порядке возрастания
@pytest.mark.parametrize(
    "expected_result",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]
    ],
)
def test_sort_by_date_rev_false(
    list_executed: List[Dict[str, Any]], expected_result: List[Dict[str, Any]]
) -> None:
    assert sort_by_date(list_executed, reverse=False) == expected_result


# Проверка корректности сортировки при одинаковых датах
@pytest.mark.parametrize(
    "expected_result",
    [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2019-07-03T18:35:29.512364",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
        ]
    ],
)
def test_sort_by_same_date_rev_true(
    list_same_date: List[Dict[str, Any]], expected_result: List[Dict[str, Any]]
) -> None:
    assert sort_by_date(list_same_date, reverse=True) == expected_result


# Тесты на работу функции с некорректными или нестандартными форматами дат
def test_sort_by_date_false(list_data_false: Any) -> None:
    with pytest.raises(ValueError, match="Некорректный или нестандартный формат даты"):
        sort_by_date(list_data_false)
