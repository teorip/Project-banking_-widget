from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    bank_transaction_data: List[Dict],
    state: str = "EXECUTED",
) -> List[Dict]:
    """Функция фильтрации словарей по значению ключа"""
    filtered_date = [
        item for item in bank_transaction_data if item.get("state") == state
    ]
    if not filtered_date:
        raise ValueError("Отсутствуют словари с указанным статусом в списке")

    return filtered_date


def sort_by_date(
    bank_transaction_data: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """Функция фильтрации словарей по дате"""
    try:
        sort_transaction_data = sorted(
            bank_transaction_data,
            key=lambda item: datetime.strptime(
                item.get("date"), "%Y-%m-%dT%H:%M:%S.%f"
            ),
            reverse=reverse,
        )
        return sort_transaction_data
    except ValueError:
        raise ValueError("Некорректный или нестандартный формат даты")
