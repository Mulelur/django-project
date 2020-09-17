from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from .models import Notification, BuildDashboard, TimeLine
from buy.models import Billing, Plan


def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance, title='Account Create')
        
post_save.connect(create_notification, sender=User)   

def building_dash(sender, instance, created, **kwargs):
    if created:
        Plan.objects.create(plan='PRESONAL')
        Plan.objects.create(plan='BUSINESS')
        Plan.objects.create(plan='ENTERPRICE')
        
post_save.connect(building_dash, sender=BuildDashboard)

def create_timeline(sender, instance, created, **kwargs):
    if created:
        regiter = TimeLine.objects.create(user=instance, register='complited')

post_save.connect(create_timeline, sender=User)        