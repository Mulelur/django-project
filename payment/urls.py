from django.urls import path

from .views import payment, charge, update_transaction_records, password_verification

urlpatterns = [
    path('', payment, name='payment'),
    path('charge/', charge, name="charge"),
    path('transaction/<token>/', update_transaction_records, name='update_records'),
    path('password_verification/', password_verification, name='password-verification')
]