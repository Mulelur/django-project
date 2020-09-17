from .models import Notification
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from buy.models import Billing

def extars(request):
    # user = get_object_or_404(User, username=request.user)
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        try:
            get_notification = Notification.objects.get(user=user)
            return {'notification': notification, 'get_notification': get_notification}
        except:
            ''

        notification = Notification.objects.filter(user=user)[:5]
    else:
        ''   
    return {}