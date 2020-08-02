from django.urls import path
from .views import buyingRegisterView, buyingPlanView, buyingRequestView, buyingPaymentView, buyingFreePlanView

urlpatterns = [
    path('', buyingRegisterView, name='buy'),
    path('buying-plan/', buyingPlanView, name='buy-plan'),
    path('buying-plan/<int:username>/', buyingFreePlanView, name='buy-plan'),
    path('buying-request/', buyingRequestView, name='buy-request'),
    path('buying-payment/', buyingPaymentView, name='buy-payment')
]