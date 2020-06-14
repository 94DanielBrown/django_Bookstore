# payments/views.py
from django.views.generic import TemplateView
from django.conf import settings
import logging
import stripe
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(TemplateView):
    template_name = 'payments/purchase.html'
    logging.debug('message')

    def get_context_data(self, **kwargs):
        logging.debug(kwargs)
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_PUBLISHABLE_KEY
        logging.error(settings.STRIPE_PUBLISHABLE_KEY)
        logging.error("Test")
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1200,
            currency='gbp',
            description='The Phoenix Project',
            source=request.POST['stripeToken']
        )
        return render(request, 'payments/charge.html')
