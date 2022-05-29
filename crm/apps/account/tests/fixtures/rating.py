import pytest
from apps.account.models import Rating


@pytest.fixture
def rating_ins(db, rating_factory) -> Rating:
    rating = rating_factory.create()
    return rating
