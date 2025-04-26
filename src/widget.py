import datetime
from typing import Union

from src import masks


def get_data(data_string: str) -> str:
    """Функция преобразовния строки из формата "2024-03-11T02:26:18.671407"
    в формат "ДД.ММ.ГГГГ" """

    date_format = datetime.datetime.strptime(data_string, "%Y-%m-%dT%H:%M:%S.%f")

    return date_format.strftime("%d.%m.%Y")


def mask_account_card(bank_details: Union[str, int]) -> str:
    """Функция маскирования карт и счетов клиента.
    Использован импорт функций их файла masks"""
    bank_details = str(bank_details)
    list_bank_details = bank_details.split(" ")
    if len(list_bank_details[-1]) == 16:
        processed_data = f"{" ".join(list_bank_details[0:-1])} {masks.get_mask_card_number(list_bank_details[-1])}"
    elif len(list_bank_details[-1]) == 20:
        processed_data = f"{" ".join(list_bank_details[0:-1])} {masks.get_mask_account(list_bank_details[-1])}"
    elif len(list_bank_details[-1]) < 16 or len(list_bank_details[-1]) < 20:
        raise ValueError("Введены не корректные данные")
    return processed_data
