import pytest
from django.urls import reverse, resolve
from .views import HomePageView


@pytest.fixture
def response(client):
    response = client.get(reverse('home'))
    return response


def test_homepage_status_code(response):
    assert response.status_code == 200


def test_homepage_url_name(response):
    assert response.status_code == 200


def test_homepage_template(response):
    assert 'home.html' in (t.name for t in response.templates)


def test_homepage_contains_correct_html(response):
    assert 'Homepage' in str(response.content)


def test_homepage_does_not_contain_incorrect_html(response):
    assert 'Some silly sentence' not in str(response.content)


def test_homepage_url_resolves_homepageview():
    view = resolve('/')
    assert view.func.__name__ == HomePageView.as_view().__name__
