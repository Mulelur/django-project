from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile, Address

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Address.objects.create(
            addres_line_1='',
            addres_line_2='',
            province='',
            country=''
        )

        
post_save.connect(create_profile, sender=User)

# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.Profile.save()        
        
# post_save.connect(update_profile, sender=User)   
# 
# def create_complument_product(sender, instance, created, **kwargs):
#     if created:
#         Compliment.objects.create(connection_with=instance)

# post_save.connect(create_complument_product, sender=Product)             