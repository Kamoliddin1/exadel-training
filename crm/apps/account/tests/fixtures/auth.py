from django.urls import reverse

import pytest
from typing import Any

from rest_framework.test import APIClient
from apps.account.models import Account

pytest_plugins = [
    "apps.account.tests.fixtures.account",

]


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
