# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, PermissionsTestView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('permissions-test/', PermissionsTestView.as_view(),
        name='permissions_test'),
]
