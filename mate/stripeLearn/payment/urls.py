from django.urls import path
from payment.views import payment

urlpatterns = [
    path('payment/', payment, name='payment'),
]
