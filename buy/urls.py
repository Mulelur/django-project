from django.urls import path
from .views import  buyingPlanView, buyingRequestView, buyingPaymentView, buyingFreePlanView, auto_renew_toggel, switch_billing_cycle, update_billing

urlpatterns = [
    # path('', buyingRegisterView, name='buy'),
    path('buying-plan/', buyingPlanView, name='buy-plan'),
    path('buying-plan/<int:username>/', buyingFreePlanView, name='buy-plan'),
    path('buying-request/', buyingRequestView, name='buy-request'),
    path('buying-payment/', buyingPaymentView, name='buy-payment'),
    path('autorenew/', auto_renew_toggel, name='auto-renew-toggel'),
    path('update_billing/', update_billing, name='update_billing'),
    path('switch_billing_cycle/', switch_billing_cycle, name='switch_billing_cycle'),
]