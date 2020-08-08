from django.urls import path

from .views import payment, create_plan, update_transaction_records, password_verification, cancel_plan

urlpatterns = [
    path('', payment, name='payment'),
    path('charge/', create_plan, name="charge"),
    path('cancel_plan/', cancel_plan, name="cancel_plan"),
    path('transaction/<token>/', update_transaction_records, name='update_records'),
    path('password_verification/', password_verification, name='password-verification')
]