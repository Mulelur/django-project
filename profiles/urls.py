from django.urls import path
from .views import profilesView

urlpatterns = [
    path('dashboard/profile/', profilesView, name='profile'),
]