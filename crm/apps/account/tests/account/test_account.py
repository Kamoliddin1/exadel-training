import pytest
from rest_framework import status
import json

pytest_plugins = [
    "apps.account.tests.fixtures.account",
    "apps.account.tests.fixtures.auth",
]
pytestmark = pytest.mark.django_db


class TestAccountEndpoints:
    url = '/accounts/'

    def test_accounts_list(self, auto_login) -> None:
        """  Test for listing all account both companies and clients  """
        client, user = auto_login()
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_accounts_retrieve(self, auto_login, create_client) -> None:
        expected_json = {
            'id': create_client.id,
            'username': create_client.username,
            'is_user': create_client.is_user,
            'is_company': create_client.is_company,
            'password': create_client.password
        }
        client, user = auto_login()
        response = client.get(f"{self.url}{create_client.id}/")
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data == expected_json

    def test_accounts_update(self, auto_login, create_client) -> None:
        expected_json = {
            "username": create_client.username,
            "password": create_client.password,
            "is_user": create_client.is_user,
            "is_company": create_client.is_company
        }
        client, user = auto_login()
        response = client.put(f"{self.url}{create_client.id}/", data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data['username'] == expected_json['username']
        assert data['is_user'] == expected_json['is_user']
        assert data['is_company'] == expected_json['is_company']

    def test_accounts_create(self, auto_login, create_client) -> None:
        expected_json = {
            "username": create_client.username + '1',
            "password": create_client.password,
            "is_user": create_client.is_user,
            "is_company": create_client.is_company
        }
        client, user = auto_login()
        response = client.post(self.url, data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_201_CREATED
        assert data['username'] == expected_json['username']
        assert data['is_user'] == expected_json['is_user']
        assert data['is_company'] == expected_json['is_company']

    def test_accounts_delete(self, auto_login, create_client) -> None:
        client, user = auto_login()
        response = client.delete(f"{self.url}{create_client.id}/", format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
