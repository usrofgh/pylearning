from django.shortcuts import render
import stripe

stripe.api_key = "sk_test_51N0hH2LQ0gHMLuBYTZUEApx04QmoWWN6jMEWLjua1RcSDPqHb4KioiIvxaocMoKgYnANxLlZUow4AI2q0oU13XTF00t1SW31JE"


def payment(request):
    if request.method == 'POST':
        amount = int(request.POST['amount']) * 100 # Convert dollars to cents
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd'
        )
        client_secret = intent.client_secret
        return render(request, 'success.html', {'client_secret': client_secret})
    else:
        return render(request, 'payment.html')
