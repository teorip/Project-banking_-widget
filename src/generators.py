def filter_by_currency(transactions: list, currency: str):
    """Фильтрует список транзакций по валюте"""
    if not transactions or not currency:
        raise ValueError("Транзакции в заданной валюте отсутствуют")
    by_currency = filter(
        lambda transaction: transaction.get("operationAmount", {})
        .get("currency", {})
        .get("code")
        == currency,
        transactions,
    )
    return by_currency


def transaction_descriptions(transactions: list):
    """Выводит список описаний транзакций"""
    if not transactions:
        raise ValueError("Введены пустые транзакции")
    description = (
        transaction.get("description")
        for transaction in transactions
        if transaction.get("description")
    )
    yield from description


def card_number_generator(start: int, end: int):
    """Генерирует номер карты в заданном диапазоне"""
    for card in range(start, end + 1):
        card = f"{card:016d}"
        card = f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
        if end >= 10000000000000000:
            raise ValueError(
                "Заданный диапазон карты не может быть больше 9999999999999999"
            )
        yield card


if __name__ == "__main__":
    print()
