from django.db import models
from django.contrib.auth.models import User
from django.db import models
import datetime
import calendar
from .country import COUNTRY

class Plan(models.Model):
    PLANS = (
        ('PRESONAL', 'PRESONAL'),
        ('BUSINESS', 'BUSINESS'),
        ('ENTERPRICE', 'ENTERPRICE')
    )
    plan = models.CharField(max_length=100, choices=PLANS)    
    
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


# class Address(models.Model):
#     addres_line_1 = models.CharField(max_length=200, blank=True)
#     addres_line_2 = models.CharField(max_length=200, blank=True)
#     province_or_sate = models.CharField(max_length=200, blank=True)
#     country = models.CharField(max_length=200, choices=COUNTRY, blank=True)
#     postal_code= models.ImageField()
#     city = models.CharField(max_length=100)

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
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='billing_user')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    billed_monthly = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, blank=True)
    ammount = models.IntegerField()
    free_trial = models.BooleanField(default=False, blank=True)

    staterd = models.DateField(auto_now_add=True)
    auto_renew = models.BooleanField(default=True, blank=True)

    # addsers

    addres_line_1 = models.CharField(max_length=200, blank=True)
    addres_line_2 = models.CharField(max_length=200, blank=True)
    province_or_sate = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, choices=COUNTRY, blank=True)
    postal_code= models.IntegerField(blank=True)
    city = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-is_active']

    def get_next_billing(self):
        tdelta = datetime.timedelta(days=30)
        month = self.staterd + tdelta
        return month

    def get_next_billing_yearly(self):
        tdelta = datetime.timedelta(days=365)
        month = self.staterd + tdelta
        return month


    # def get_month_and_days_rimaing():
    #     tdelta = datetime.timedelta(days=30)
    #     today = datetime.date.today()
    #     days_in_current_month = calendar.monthrange(today._year, today.month)[1]
    #     days_till_end_month = days_in_current_month - today.day
    #     end_of_the_month = days_till_end_month
    #     day = end_of_the_month - today
    #     return day
    def get_day(self):
        tdelta = datetime.timedelta(days=30)
        month = self.staterd + tdelta
        today = datetime.date.today()
        return month - today

    def get_monthly_ammount(self):
        return self.ammount

    def get_yearly(self):
        return sum([self.ammount * 12 * 0.7 ])

    def get_next_billing_monthly(self):
        return self.staterd

    def get_user_plan(self):
        return self.plan    


class Transaction(models.Model):
    STATUS = (
        ('active', 'active'),
        ('canceled', 'canceled'),
        ('pending', 'pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=120)
    # subscription_id = models.CharField(max_length=1000, default='')
    billing_id = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.CharField(max_length=100, choices=STATUS, default='active')

    def __str__(self):
        return self.billing_id

    class Meta:
        ordering = ['-timestamp']

    def get_expaitry_day(self):
        tdelta = datetime.timedelta(days=30)
        return self.timestamp + tdelta 
