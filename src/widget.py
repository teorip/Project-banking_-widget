import datetime

from src.masks import get_mask_account, get_mask_card_number


def get_data(data_string: str) -> str:
    """Функция преобразовния строки из формата "2024-03-11T02:26:18.671407"
    в формат "ДД.ММ.ГГГГ" """
    try:
        date_format = datetime.datetime.strptime(data_string, "%Y-%m-%dT%H:%M:%S.%f")

        return date_format.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")


def mask_account_card(bank_details: int) -> str:
    """Функция маскирования карт и счетов клиента.
    Использован импорт функций их файла masks"""

    bank_details = str(bank_details)
    list_bank_details = bank_details.split(" ")
    last_element = list_bank_details[-1]

    if last_element.isnumeric() and len(last_element) == 16:
        processed_data_card = (
            f"{" ".join(list_bank_details[0:-1])} {get_mask_card_number(last_element)}"
        )
        return processed_data_card
    elif last_element.isnumeric() and len(last_element) == 20:
        processed_data_account = (
            f"{" ".join(list_bank_details[0:-1])} {get_mask_account(last_element)}"
        )
        return processed_data_account
    else:
        raise ValueError("Введеные банковские данные не корректны")
