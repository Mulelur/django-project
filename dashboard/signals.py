from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from .models import Notification


def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance, title='Account Create')
        
post_save.connect(create_notification, sender=User)   