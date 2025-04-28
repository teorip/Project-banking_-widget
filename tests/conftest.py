from typing import Any, Dict, List

import pytest


@pytest.fixture
def card_number() -> int:
    return 7000792289606361


@pytest.fixture
def card_number_false() -> Any:
    return "70007ffff89606361"


@pytest.fixture
def data() -> str | int:
    return format("%Y-%m-%dT%H:%M:%S.%f")


@pytest.fixture
def data_false() -> Any:
    return format("%Y%m-%dT%H:%M%S.%f")


# @pytest.fixture
# def bank_details_fixture() -> int:
#     return 73654108430135874305


@pytest.fixture
def bank_details_false() -> Any:
    return "73654108ddd358743050"


@pytest.fixture
def account() -> int:
    return 73654108430135874305


@pytest.fixture
def account_len_false() -> int:
    return 736541084301358743


@pytest.fixture
def account_format_false() -> Any:
    return "73654108430sddd1358743"


@pytest.fixture
def list_no_executed() -> List[Dict[str, Any]]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_executed() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_same_date() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_data_false() -> List[Dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T1835:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]
