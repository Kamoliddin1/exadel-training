import pytest
from rest_framework import status
import json

pytest_plugins = [
    # "apps.account.tests.fixtures.account",
    "apps.account.tests.fixtures.user",
    "apps.account.tests.fixtures.city",
    "apps.account.tests.fixtures.auth",
]
pytestmark = pytest.mark.django_db


class TestUserEndpoints:
    url = '/users/'

    def test_user_list(self, auto_login) -> None:
        """  Test for listing all users(clients)  """
        client, user = auto_login()
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_user_retrieve(self, auto_login, user_ins, city_ins) -> None:
        client, user = auto_login()
        expected_json = {
            'user': user_ins.pk,
            'username': user_ins.user.username,
            'house_number': user_ins.house_number,
            'total_area': user_ins.total_area,
            'street': user_ins.street,
            'city': user_ins.city_id
        }

        response = client.get(f"{self.url}{user_ins.pk}/")
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data['user'] == expected_json['user']
        assert data['username'] == expected_json['username']
        assert data['house_number'] == expected_json['house_number']
        assert data['total_area'] == expected_json['total_area']
        assert data['street'] == expected_json['street']
        assert data['city'] == expected_json['city']

    def test_user_create(self, auto_login, user_ins) -> None:
        client, user = auto_login()

        expected_json = {
            'user': 1,
            'house_number': user_ins.house_number,
            'total_area': user_ins.total_area,
            'street': user_ins.street,
            'city': user_ins.city_id
        }
        response = client.post(self.url, data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_201_CREATED
        assert data['user'] == expected_json['user']
        assert data['city'] == expected_json['city']
        assert data['street'] == expected_json['street']
        assert data['house_number'] == expected_json['house_number']

    def test_user_update(self, auto_login, user_ins) -> None:
        expected_json = {
            'user': 1,
            'house_number': user_ins.house_number,
            'total_area': user_ins.total_area,
            'street': user_ins.street,
            'city': user_ins.city_id
        }
        client, user = auto_login()
        response = client.put(f"{self.url}{user_ins.pk}/", data=expected_json, format='json')
        data = json.loads(response.content)
        assert data['user'] == expected_json['user']
        assert data['city'] == expected_json['city']
        assert data['street'] == expected_json['street']
        assert data['house_number'] == expected_json['house_number']

    def test_company_delete(self, auto_login, user_ins) -> None:
        client, user = auto_login()
        response = client.delete(f"{self.url}{user_ins.pk}/", format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
