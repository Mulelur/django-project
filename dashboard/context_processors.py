from .models import Notification
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

def extars(request):
    user = get_object_or_404(User, username=request.user)
    notification = Notification.objects.filter(user=user)[:5]
    try:
        get_notification = Notification.objects.get(user=user)
    except:
        get_notification = None
        messages.info(request, 'no notification') 

    return {'notification': notification, 'get_notification': get_notification}