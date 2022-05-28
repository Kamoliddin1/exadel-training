import pytest
from rest_framework import status
import json

from rest_framework.reverse import reverse

pytest_plugins = [
    "apps.account.tests.fixtures.user",

]


@pytest.mark.django_db
def test_accounts_list(auto_login) -> None:
    """  Test for listing all account both companies and clients  """
    url = '/accounts/'
    client, user = auto_login()
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
