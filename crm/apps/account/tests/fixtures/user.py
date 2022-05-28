from django.urls import reverse

import pytest
from typing import Any

from rest_framework.test import APIClient
from apps.account.models import Account, User


@pytest.fixture
def create_client(db) -> Account:
    """
    Create client user
    :return: User instance
    """
    user_data = {
        "username": 'kamoliddin',
        "is_user": True,
        "is_company": False,
    }
    make_user, _ = Account.objects.get_or_create(**user_data)
    make_user.set_password('147007')
    make_user.save()
    return make_user


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
