from django.contrib.auth import get_user_model
import pytest


@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(
        username='will',
        email='will@email.com',
        password='testpass123'
    )
    assert user.username == 'will'
    assert user.email == 'will@email.com'
    assert user.is_active
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_super_user():
    User = get_user_model()
    admin_user = User.objects.create_superuser(
        username='superadmin',
        email='superadmin@email.com',
        password='testpass123'
    )
    assert admin_user.username == 'superadmin'
    assert admin_user.email == 'superadmin@email.com'
    assert admin_user.is_active
    assert admin_user.is_superuser
