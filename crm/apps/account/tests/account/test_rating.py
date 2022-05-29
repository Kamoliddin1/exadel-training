import pytest
from rest_framework import status
import json

pytest_plugins = [
    "apps.account.tests.fixtures.account",
    "apps.account.tests.fixtures.rating",
    "apps.account.tests.fixtures.auth",
]
pytestmark = pytest.mark.django_db


class TestBranchEndpoints:
    url = '/ratings/'

    def test_ratings_list(self, auto_login) -> None:
        """  Test for listing all branches """
        client, user = auto_login()
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_ratings_retrieve(self, auto_login, rating_ins) -> None:
        now = rating_ins.timestamp
        expected_json = {
            'id': rating_ins.id,
            'author': rating_ins.author_id,
            'rate': rating_ins.rate,
            'review': rating_ins.review,
            'timestamp': now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        client, user = auto_login()
        response = client.get(f"{self.url}{rating_ins.id}/")
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data == expected_json

    def test_ratings_create(self, auto_login, rating_ins) -> None:
        expected_json = {
            'id': rating_ins.id,
            'author': rating_ins.author.user_id,
            'rate': rating_ins.rate,
            'review': rating_ins.review,
            'timestamp': rating_ins.timestamp,
        }
        client, user = auto_login()
        response = client.post(self.url, data=expected_json, format='json')
        data = json.loads(response.content)
        print(response.content)
        assert response.status_code == status.HTTP_201_CREATED
        assert data['author'] == expected_json['author']
        assert data['rate'] == expected_json['rate']
        assert data['review'] == expected_json['review']

    def test_ratings_update(self, auto_login, rating_ins) -> None:
        expected_json = {
            'id': rating_ins.id,
            'author': rating_ins.author.user_id,
            'rate': rating_ins.rate,
            'review': rating_ins.review,
            'timestamp': rating_ins.timestamp,
        }
        client, user = auto_login()
        response = client.put(f"{self.url}{rating_ins.pk}/", data=expected_json, format='json')
        data = json.loads(response.content)
        assert response.status_code == status.HTTP_200_OK
        assert data['author'] == expected_json['author']
        assert data['rate'] == expected_json['rate']
        assert data['review'] == expected_json['review']

    def test_ratings_delete(self, auto_login, rating_ins) -> None:
        client, user = auto_login()
        response = client.delete(f"{self.url}{rating_ins.pk}/", format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
