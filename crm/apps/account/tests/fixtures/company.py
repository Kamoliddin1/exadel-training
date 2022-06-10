import pytest
from apps.account.models import Company


@pytest.fixture
def create_company_ins(db, company_factory) -> Company:
    company = company_factory.create()
    return company
