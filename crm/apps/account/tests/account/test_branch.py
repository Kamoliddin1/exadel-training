import pytest
from rest_framework import status
import json

pytest_plugins = [
    "apps.account.tests.fixtures.account",
    "apps.account.tests.fixtures.branch",
    "apps.account.tests.fixtures.auth",
]
pytestmark = pytest.mark.django_db


class TestBranchEndpoints:
    url = '/branches/'

    def test_branches_list(self, auto_login) -> None:
        """  Test for listing all branches """
        client, user = auto_login()
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_branch_retrieve(self, auto_login, branch_ins) -> None:
        expected_json = {
            'id': branch_ins.id,
            'name': branch_ins.name,
            'company': branch_ins.company_id,
            'company_name': branch_ins.company.title
        }
        client, user = auto_login()
        response = client.get(f"{self.url}{branch_ins.id}/")
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data == expected_json

    def test_branch_create(self, auto_login, branch_ins) -> None:
        expected_json = {
            'id': branch_ins.id,
            'name': branch_ins.name,
            'company': branch_ins.company_id
        }
        client, user = auto_login()
        response = client.post(self.url, data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_201_CREATED
        assert data['company'] == expected_json['company']
        assert data['name'] == expected_json['name']

    def test_branch_update(self, auto_login, branch_ins) -> None:
        expected_json = {
            'id': branch_ins.id,
            'name': branch_ins.name,
            'company': branch_ins.company_id
        }
        client, user = auto_login()
        response = client.put(f"{self.url}{branch_ins.pk}/", data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data['name'] == expected_json['name']
        assert data['company'] == expected_json['company']

    def test_branch_delete(self, auto_login, branch_ins) -> None:
        client, user = auto_login()
        response = client.delete(f"{self.url}{branch_ins.pk}/", format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
