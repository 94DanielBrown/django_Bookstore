# books/tests.py
from django.urls import reverse
import pytest
from .models import Book


# Book creation test
@pytest.mark.django_db
def test_create_book(client):
    book = Book.objects.create(
        title='Django for professionals',
        author='William S. Vincent',
        price='30.00',
    )
    assert book.title == 'Django for professionals'
    assert book.author == 'William S. Vincent'
    assert book.price == '30.00'

    response = client.get(reverse('book_list'))
    assert response.status_code == 200
    assert 'Django for professionals' in str(response.content)

    response = client.get(book.get_absolute_url())
    no_response = client.get('/books/12345')
    assert response.status_code == 200
    assert no_response.status_code == 404 
