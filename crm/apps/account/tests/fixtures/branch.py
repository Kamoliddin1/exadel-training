import pytest
from apps.account.models import Branch


@pytest.fixture
def branch_ins(db, branch_factory) -> Branch:
    branch = branch_factory.create()
    return branch
