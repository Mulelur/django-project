from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from .models import Plan

def plan(sender, instance, created, **kwargs):
    pass

# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.Profile.save()        
        
# post_save.connect(update_profile, sender=User)   
# 
# def create_complument_product(sender, instance, created, **kwargs):
#     if created:
#         Compliment.objects.create(connection_with=instance)

# post_save.connect(create_complument_product, sender=Product)             