from django.urls import path
from .views import (
 dashboard,
 personal_info,
 billing,
 settings,
 notification,
 subscriptions,
 payment_hestory,
 pricing,
 invoices,
 invoices_detail,
 support,
 faqs,
 contact,
 invoices_print,
 subscriptions_detail
 )

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('personal_info/', personal_info, name='personal-info'),
    path('billing/', billing, name='billing'),
    path('settings/', settings, name='settings'),
    path('notification/', notification, name='notification'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('subscriptions/<int:id>/', subscriptions_detail, name='subscriptions-detail'),
    path('payment_hestory/', payment_hestory, name='payment-hestory'),
    path('pricing/', pricing, name='pricing'),
    path('invoices/', invoices, name='invoices'),
    path('invoices/<int:id>/', invoices_detail, name='invoices-detail'),
    path('invoices_print/<int:id>/', invoices_print, name='invoices-print'),
    path('support/', support, name='support'),
    path('faqs/', faqs, name='faqs'),
    path('contact/', contact, name='contact'),

]