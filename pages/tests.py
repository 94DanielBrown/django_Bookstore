import pytest
from django.urls import reverse


def test_homepage_status_code(client):
    response = client.get('/')
    assert response.status_code == 200


def test_homepage_url_name(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200


def test_homepage_template(client):
    response = client.get('/')
    assert 'home.html' in (t.name for t in response.templates)


def test_homepage_contains_correct_html(client):
    response = client.get('/')
    assert 'Homepage' in str(response.content)


def test_homepage_does_not_contain_incorrect_html(client):
    response = client.get('/')
    assert 'Some silly sentence' not in str(response.content)
