import pytest
from apps.account.models import City


@pytest.fixture
def city_ins(db, city_factory) -> City:
    city = city_factory.create()
    return city
