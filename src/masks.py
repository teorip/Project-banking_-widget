def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""

    card_str = str(card_number)
    if card_str.isnumeric() and len(card_str) == 16:
        masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        return masked_card
    else:
        raise ValueError("Номер карты должен содержать только цифры и равен 16 цифрам")


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его маску."""

    account_str = str(account_number)
    if account_str.isnumeric() and len(account_str) == 20:
        masked_account = f"**{account_str[-4:]}"
        return masked_account
    else:
        raise ValueError("Номер счёта должен содержать только цифры и равен 20 цифрам.")


if __name__ == "__main__":
    print()
