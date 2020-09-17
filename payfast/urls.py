from django.urls import path
from .views import cheackout_view

urlpatterns = [
    path('', cheackout_view, name='cheackout')
]