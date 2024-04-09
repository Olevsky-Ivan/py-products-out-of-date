import pytest
import datetime

from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        },
    ]


@pytest.mark.parametrize(
    "expiration_date, expected",
    [
        (datetime.date(2022, 2, 10), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 5), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 1), ["salmon", "chicken", "duck"])
    ]
)
def test_expiration_date(
        products: list,
        expiration_date: datetime.date,
        expected: list[str]
) -> None:
    with patch("datetime.datetime") as mocked_datetime:
        mocked_datetime.today.return_value = datetime.datetime(
            expiration_date.year,
            expiration_date.month,
            expiration_date.day
        )
        assert outdated_products(products) == expected
