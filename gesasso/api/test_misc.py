# from django.test import TestCase
from uuid import UUID

import pytest
import responses
from rest_framework.test import APIRequestFactory

from gesasso import settings
from gesasso.api.factories import RequestFactory
from gesasso.api.models import Asso
from gesasso.api.views import AssosViewSet


@pytest.fixture(scope="session")
def api_rf():
    return APIRequestFactory()


@pytest.fixture
def request_data():
    return RequestFactory()


@pytest.fixture(scope="session")
def _request_mock(_request_mock_portail_auth):
    class RequestsMock(responses.RequestsMock):
        @property
        def calls(self):
            return [
                c
                for c in self._calls
                if c.request.url != _request_mock_portail_auth.url
            ]

    return RequestsMock()


@pytest.fixture(scope="session")
def _request_mock_portail_auth():
    response = responses.Response(
        "POST",
        settings.OAUTH_CLIENT["access_token_url"],
        body='{"access_token": "foobar"}',
    )
    response.call_count += 1
    return response


@pytest.fixture
def request_mock(_request_mock, _request_mock_portail_auth):
    _request_mock.add(_request_mock_portail_auth)
    with _request_mock as rsps:
        yield rsps


@pytest.fixture
def asso_viewset_get():
    return AssosViewSet.as_view(
        {
            "get": "list",
        },
        permission_classes=[],
        authentication_classes=[],
    )


@pytest.mark.django_db
def test_get_assos(api_rf, request_mock, asso_viewset_get):
    """
    Test that the get_request function returns the correct request
    """
    request = api_rf.get("/")
    request_mock.add(
        "GET",
        f'{settings.OAUTH_CLIENT["api_base_url"]}/assos',
        json=[
            {
                "id": "6dff8940-3af5-11e9-a76b-d5944de919ff",
                "login": "bde",
                "shortname": "BDE-UTC",
                "name": "Bureau Des Etudiants de l'UTC",
                "image": "https://assos.utc.fr/images/assos/6dff8940-3af5-11e9-a76b-d5944de919ff/1586527271.png",
                "deleted_at": None,
                "in_cemetery_at": None,
                "parent": None,
            },
            {
                "id": "6e105220-3af5-11e9-95ce-1f406c6cfae9",
                "login": "simde",
                "shortname": "SiMDE",
                "name": "Le Service informatique de la Maison des Étudiants",
                "image": "https://assos.utc.fr/images/assos/6e105220-3af5-11e9-95ce-1f406c6cfae9/1583931369.png",
                "deleted_at": None,
                "in_cemetery_at": None,
                "parent": {
                    "id": "6dff8940-3af5-11e9-a76b-d5944de919ff",
                    "login": "bde",
                    "shortname": "BDE-UTC",
                    "name": "Bureau Des Etudiants de l'UTC",
                    "image": "https://assos.utc.fr/images/assos/6dff8940-3af5-11e9-a76b-d5944de919ff/1586527271.png",
                    "deleted_at": None,
                    "in_cemetery_at": None,
                },
            },
        ],
    )
    response = asso_viewset_get(request)
    assert response.status_code == 200
    assert len(response.data) == 2
    assert Asso.objects.all().count() == 2
    asso = Asso.objects.get(id="6e105220-3af5-11e9-95ce-1f406c6cfae9")
    assert isinstance(asso, Asso)
    assert asso.name == "Le Service informatique de la Maison des Étudiants"
    assert asso.login == "simde"
    assert asso.shortname == "SiMDE"
    assert asso.id == UUID("6e105220-3af5-11e9-95ce-1f406c6cfae9")
    assert asso.parent.id == UUID("6dff8940-3af5-11e9-a76b-d5944de919ff")
