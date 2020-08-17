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
 subscriptions_detail,
 usernameform_View
 )
from .userchangeviews import (
    user_change_full_names,
    user_chage_username,
    user_chage_phone,
    user_chage_date_of_birth,
    user_chage_addrese)

from .notification import delete_notification_view
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
    path('usernameform/', usernameform_View, name='usernameform_view'),
    path('full_names/', user_change_full_names, name='user_change_full_names'),
    path('usernames/', user_chage_username, name='user_chage_username'),
    path('user_chage_phone/', user_chage_phone, name='user_chage_phone'),
    path('user_chage_date_of_birth/', user_chage_date_of_birth, name='user_chage_date_of_birth'),
    path('user_chage_addrese/', user_chage_addrese, name='user_chage_addrese'),
    path('remove_notification/<id>/', delete_notification_view, name='remove_notification')
]