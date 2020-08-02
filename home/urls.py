from django.urls import path
from .views import homeView, pricingView, aboutView

app_name = 'home'

urlpatterns = [
    path('', homeView, name='home'),
    path('pricing/', pricingView, name='pricing'),
    path('about/', aboutView, name='about'), 
]