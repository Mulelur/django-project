from django.shortcuts import redirect, get_object_or_404
from .models import Notification
from django.contrib.auth.models import User
from django.contrib import messages

def delete_notification_view(request, id):
    user = get_object_or_404(User, username=request.user)
    notification = Notification.objects.get(user=user)
    if notification:
        obj = notification.delete()
        messages.success(request, 'Notification removed')
        return redirect('dashboard')
    else:
        return redirect('dashboard')    