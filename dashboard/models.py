from django.db import models
from django.db import models
from django.contrib.auth.models import User
from buy.models import Plan, Request


class Notification(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    time = models.TimeField()
    read = models.BooleanField(default=False)

    # User notification_settings 

    unusual_activity = models.BooleanField(blank=True, default=True)
    new_browser = models.BooleanField(blank=True, default=True)

    sales_and_latest_news = models.BooleanField(blank=True, default=True)
    features_and_updates = models.BooleanField(blank=True, default=True)
    tips = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.title

class WebSite(models.Model):
    INDASTRY = (
        ('eCommerce','eCommerce'),
        ('Business','Business'),
        ('Entertainment','Entertainment'),
        ('Portfolio','Portfolio'),
        ('Media','Media'),
        ('Brochure','Brochure'),
        ('Nonprofit','Nonprofit'),
        ('Educational','Educational'),
        ('Infopreneur','Infopreneur'),
        ('Personal','Personal'),
        ('Web Portal','Web Portal'),
        ('Wiki or Community Forum','Wiki or Community Forum'),
        
    )
    name = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, choices=INDASTRY)
    domain = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='website_user', default='')

    def __str__(self):
        return self.name

        
class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_websites = models.ForeignKey(WebSite, on_delete=models.CASCADE, default='', null=True, blank=True)
    


    def __str__(self):
        return f'{self.user.username} Profile'
