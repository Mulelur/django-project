from django.urls import path
from . import views as help_views

urlpatterns = [
    path('', help_views.support, name='help'),
    path('faqs/', help_views.faqs, name='faqs'),
]