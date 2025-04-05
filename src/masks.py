from typing import Union


def get_mask_card_number(card_number: Union[int]) -> [str]:
    """Принимает на вход номер карты и возвращает ее маску."""

    card_str = str(card_number)

    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"

    return masked_card


def get_mask_account(account_number: Union[int]) -> [str]:
    """Принимает на вход номер счета и возвращает его маску."""

    account_str = str(account_number)

    masked_account = f"**{account_str[-4:]}"

    return masked_account
