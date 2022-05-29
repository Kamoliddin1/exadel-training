import pytest
from rest_framework import status
import json

pytest_plugins = [
    "apps.account.tests.fixtures.account",
    "apps.account.tests.fixtures.city",
    "apps.account.tests.fixtures.auth",
]
pytestmark = pytest.mark.django_db


class TestCityEndpoints:
    url = '/cities/'

    def test_city_list(self, auto_login) -> None:
        """  Test for listing all cities """
        client, user = auto_login()
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_city_retrieve(self, auto_login, city_ins) -> None:
        expected_json = {
            'id': city_ins.id,
            'country': city_ins.country_id,
            'name': city_ins.name
        }
        client, user = auto_login()
        response = client.get(f"{self.url}{city_ins.id}/")
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data == expected_json

    def test_city_create(self, auto_login, city_ins) -> None:
        expected_json = {
            'country': city_ins.country_id,
            'name': city_ins.name
        }
        client, user = auto_login()
        response = client.post(self.url, data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_201_CREATED
        assert data['country'] == expected_json['country']
        assert data['name'] == expected_json['name']

    def test_city_update(self, auto_login, city_ins) -> None:
        expected_json = {
            'country': city_ins.country_id,
            'name': city_ins.name
        }
        client, user = auto_login()
        response = client.put(f"{self.url}{city_ins.pk}/", data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data['name'] == expected_json['name']

    def test_country_delete(self, auto_login, city_ins) -> None:
        client, user = auto_login()
        response = client.delete(f"{self.url}{city_ins.pk}/", format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
