from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Plan(models.Model):
    PLANS = (
        ('PRESONAL', 'PRESONAL'),
        ('BUSINESS', 'BUSINESS'),
        ('ENTERPRICE', 'ENTERPRICE')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    plan = models.CharField(max_length=100, choices=PLANS)
    free_trial = models.BooleanField(default=False, blank=True)
    

    def __str__(self):
        return self.plan


class Request(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    type_of_webSite_you_want = models.CharField(max_length=100, choices=INDASTRY)
    a_short_description_of_your_website = models.TextField()

    def __str__(self):
        return self.type_of_webSite_you_want


class Billing(models.Model):
    STATUS = (
        ('ACTIVE', 'ACTIVE'),
        ('EXPRIED', 'EXPRIED')
    )
    # TREAM = (
    #     ('MOUNTHLY', 'MOUNTHLY'),
    #     ('YAERLY', 'YAERLY')
    # )
    # MONTHLY_PRICE = (
    #     ('presonal(R175)','presonal(R175)'),
    #     ('business(R350)', 'business(R350)'),
    #     ('enterprice(R780)', 'enterprice(R780)')
    # )
    # YERLY_PRICE = (
    #     ('presonal(R175)','presonal(R175)'),
    #     ('business(R350)', 'business(R350)'),
    #     ('enterprice(R780)', 'enterprice(R780)')
    # )
    AMMOUNT = (
        ('175', '175'),
        ('350', '350'),
        ('780', '780')
    )
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='billing_user')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    billed = models.BooleanField()
    status = models.CharField(max_length=50, choices=STATUS, default='ACTIVE', blank=True)
    ammount = models.IntegerField()

    staterd = models.DateField(auto_now_add=True)
    auto_renew = models.BooleanField(default=True, blank=True)


    def get_monthly_ammount(self):
        return self.ammount

    def get_yearly(self):
        return sum([self.ammount * 12 * 0.7 ])

    def get_next_billing_monthly(self):
        return self.staterd



