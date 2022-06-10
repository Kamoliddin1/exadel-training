import pytest
from apps.account.models import User


@pytest.fixture
def user_ins(db, user_factory) -> User:
    user = user_factory.create()
    return user
