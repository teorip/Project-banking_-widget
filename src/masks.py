from typing import Union


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""

    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"

    return masked_card


def get_mask_account(account_number: Union[str | int]) -> str:
    """Принимает на вход номер счета и возвращает его маску."""

    account_str = str(account_number)
    if len(account_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры.")
    masked_account = f"**{account_str[-4:]}"

    return masked_account


if __name__ == "__main__":
    print()
