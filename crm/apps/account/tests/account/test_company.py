import pytest
from rest_framework import status
import json

pytest_plugins = [
    "apps.account.tests.fixtures.account",
    "apps.account.tests.fixtures.company",
    "apps.account.tests.fixtures.auth",
]
pytestmark = pytest.mark.django_db


class TestCompanyEndpoints:
    url = '/companies/'

    def test_company_list(self, auto_login) -> None:
        """  Test for listing all account both companies and clients  """
        client, user = auto_login()
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_company_retrieve(self, auto_login, create_company_ins) -> None:
        expected_json = {
            'title': create_company_ins.title,
            'company': create_company_ins.company_id,
            'street': create_company_ins.street,
            'city': create_company_ins.city_id
        }
        client, user = auto_login()
        response = client.get(f"{self.url}{create_company_ins.pk}/")
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data == expected_json

    def test_company_create(self, auto_login, create_company_ins) -> None:
        expected_json = {
            'company': int(create_company_ins.company_id)-1,
            'title': create_company_ins.title,
            'street': create_company_ins.street,
            'city': create_company_ins.city_id
        }
        client, user = auto_login()
        response = client.post(self.url, data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_201_CREATED
        assert data['title'] == expected_json['title']
        assert data['street'] == expected_json['street']
        assert data['city'] == expected_json['city']

    def test_company_update(self, auto_login, create_company_ins) -> None:
        expected_json = {
            'company': create_company_ins.pk,
            'title': create_company_ins.title,
            'street': create_company_ins.street,
            'city': create_company_ins.city_id
        }
        client, user = auto_login()
        response = client.put(f"{self.url}{create_company_ins.pk}/", data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data['title'] == expected_json['title']
        assert data['street'] == expected_json['street']
        assert data['city'] == expected_json['city']

    def test_company_delete(self, auto_login, create_company_ins) -> None:
        client, user = auto_login()
        response = client.delete(f"{self.url}{create_company_ins.pk}/", format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
