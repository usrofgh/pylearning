import stripe
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = 'sk_test_51N0hH2LQ0gHMLuBYTZUEApx04QmoWWN6jMEWLjua1RcSDPqHb4KioiIvxaocMoKgYnANxLlZUow4AI2q0oU13XTF00t1SW31JE'


@method_decorator(csrf_exempt, name='dispatch')
class TestSectionView(View):
    def post(self, request):
        # Retrieve the amount from the form
        amount = request.POST['amount']

        # Create a Stripe PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=int(amount) * 100,
            currency='usd',
            metadata={'integration_check': 'accept_a_payment'},
        )

        # Return the PaymentIntent client secret to the client
        return JsonResponse({'client_secret': intent.client_secret})
