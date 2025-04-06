import datetime


def get_data(data_string: str) -> str:
    """Функция преобразовния строки из формата "2024-03-11T02:26:18.671407"в формат "ДД.ММ.ГГГГ" """
    date_format = datetime.datetime.strptime(data_string, "%Y-%m-%dT%H:%M:%S.%f")
    return date_format.strftime("%d.%m.%Y")
