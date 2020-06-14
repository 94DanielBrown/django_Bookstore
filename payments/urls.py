# payments/urls.py
from django.urls import path

from .views import PaymentView, charge


urlpatterns = [
    path('', PaymentView.as_view(), name='payments'),
    path('charge/', charge, name='charge'),
]
