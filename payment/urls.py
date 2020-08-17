from django.urls import path

from .views import payment, create_plan, update_transaction_records, cancel_plan

urlpatterns = [
    path('', payment, name='payment'),
    path('charge/', create_plan, name="charge"),
    path('transaction/<token>/', update_transaction_records, name='update_records'),
]