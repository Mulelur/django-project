from django.urls import path
from .views import  (buyingPlanView,
                         billingInfoView,
                         buyingRequestView,
                         buyingPaymentView,
                         buyingFreePlanView,
                         auto_renew_toggel, switch_billing_cycle,
                         update_billing,
                         billing_cancel_view,
                         thank_you,
                         cancel_confirm,
                         rewnew_confirm,
                         rewnew_billing,
                         get_started)
from payfast.views import cheackout_view
urlpatterns = [
    # path('', buyingRegisterView, name='buy'),
    path('buying-plan/', buyingPlanView, name='buy-plan'),
    path('buying-billon-info/', billingInfoView, name='billon-info'),
    path('buying-plan/<int:username>/', buyingFreePlanView, name='buy-plan'),
    path('buying-request/', buyingRequestView, name='buy-request'),
    path('buying-payment/', buyingPaymentView, name='buy-payment'),
    path('autorenew/', auto_renew_toggel, name='auto-renew-toggel'),
    path('update_billing/', update_billing, name='update_billing'),
    path('switch_billing_cycle/', switch_billing_cycle, name='switch_billing_cycle'),
    path('cancel-subscription/', billing_cancel_view, name='cancel-subscription'),
    path('rewnew_billing/<int:id>/', rewnew_billing, name='rewnew_billing'),
    path('thank-you/', thank_you, name='thank_you'),
    path('cancel_confirm/', cancel_confirm, name='cancel_confirm'),
    path('rewnew_confirm', rewnew_confirm, name='rewnew_confirm'),
    path('get_started/', get_started, name='get_started')
]