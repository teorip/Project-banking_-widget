from typing import Dict, List


def filter_by_state(
    bank_transaction_data: List[Dict], state: str = "EXECUTED"
) -> List[Dict]:
    """Функция фильтрации словарей по значению ключа"""

    return [item for item in bank_transaction_data if item.get("state") == state]
