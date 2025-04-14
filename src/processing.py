from typing import Any, Dict, List


def filter_by_state(
    bank_transaction_data: List[Dict], state: str = "EXECUTED"
) -> List[Dict]:
    """Функция фильтрации словарей по значению ключа"""

    return [item for item in bank_transaction_data if item.get("state") == state]


def sort_by_date(
    bank_transaction_data: List[Dict[str, Any]], reverse: bool = True
) -> List:
    """Функция фильтрации словарей по дате"""

    return sorted(
        bank_transaction_data, key=lambda item: item.get("date"), reverse=reverse
    )
