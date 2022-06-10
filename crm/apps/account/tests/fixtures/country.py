import pytest
from apps.account.models import Country


@pytest.fixture
def country_ins(db, country_factory) -> Country:
    country = country_factory.create()
    return country
