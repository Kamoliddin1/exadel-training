import pytest
from apps.account.models import Account


@pytest.fixture
def create_client(db, account_client_factory) -> Account:
    """
    Create client user
    :return: Account instance
    """
    make_user = account_client_factory.build()
    make_user.set_password('147007')
    make_user.save()
    return make_user


@pytest.fixture
def create_company(db, account_company_factory) -> Account:
    """
    Create company user
    :return: Account instance
    """
    make_company = account_company_factory.create()
    make_company.set_password('147007')
    make_company.save()
    return make_company
