import pytest
from rest_framework import status
import json

pytest_plugins = [
    "apps.account.tests.fixtures.account",
    "apps.account.tests.fixtures.country",
    "apps.account.tests.fixtures.auth",
]
pytestmark = pytest.mark.django_db


class TestCountryEndpoints:
    url = '/countries/'

    def test_country_list(self, auto_login) -> None:
        """  Test for listing all countries """
        client, user = auto_login()
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_country_retrieve(self, auto_login, country_ins) -> None:
        expected_json = {
            'id': country_ins.id,
            'name': country_ins.name,
        }
        client, user = auto_login()
        response = client.get(f"{self.url}{country_ins.id}/")
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data == expected_json

    def test_country_create(self, auto_login, country_ins) -> None:
        expected_json = {
            'name': country_ins.name,
        }
        client, user = auto_login()
        response = client.post(self.url, data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_201_CREATED
        assert data['name'] == expected_json['name']

    def test_country_update(self, auto_login, country_ins) -> None:
        expected_json = {
            'name': country_ins.name
        }
        client, user = auto_login()
        response = client.put(f"{self.url}{country_ins.pk}/", data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data['name'] == expected_json['name']

    def test_country_delete(self, auto_login, country_ins) -> None:
        client, user = auto_login()
        response = client.delete(f"{self.url}{country_ins.pk}/", format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
