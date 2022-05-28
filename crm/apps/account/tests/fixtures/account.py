from django.urls import reverse

import pytest
from typing import Any

from rest_framework.test import APIClient
from apps.account.models import Account


@pytest.fixture
def create_client(db, account_client_factory) -> Account:
    """
    Create client user
    :return: Account instance
    """
    make_user = account_client_factory.create()
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


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def token(create_client: Account,
          api_client: APIClient):
    """
    Create token
    :return: token
    """
    user = create_client
    login_data = {
        "username": user.username,
        "password": '147007'
    }
    # get token
    token_url = reverse('token_obtain_pair')
    token = api_client.post(token_url, login_data, format='json')
    return token


@pytest.fixture
def auto_login(
        db,
        api_client: APIClient,
        create_client: Account,
        token
) -> Any:
    """
    Token based auto login admin
    :return: client, user
    """

    def make_auto_login(user=None):
        # check that access token was sent in response
        assert token.data['access'] is not None
        # add http authorization header with Bearer prefix
        if user is None:
            user = create_client
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.data["access"]}', format='json')
        return api_client, user

    return make_auto_login
