from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# paypast model

class MerchantDetail(models.Model):
    # The Merchant ID as given by the PayFast system.
    #  Used to uniquely identify the receiving account.

    # This can be found on the merchant’s settings page.
    merchant_id = models.IntegerField(blank=True, null=True)
    # The Merchant Key as given by the PayFast system.
    # Used to uniquely identify the receiving account.
    # This provides an extra level of certainty concerning the correct account as both the ID and the Key must be correct in order for the transaction to proceed.
    # This can be found on the merchant’s settings page.
    merchant_key = models.CharField(max_length=500, blank=True)

    def __str__():
        return 'merchant details'

class MerchantUrl(models.Model):
    # The URL where the user is returned to after payment has been successfully taken.
    return_url = models.URLField(blank=True, default=settings.RETURN_URL)
    # The URL where the user should be redirected should they choose to cancel their payment while on the PayFast system.
    cancel_url = models.URLField(blank=True, default=settings.CANCEL_URL)
    # The URL which is used by PayFast to post the Instant Transaction Notifications (ITNs) for this transaction.
    notify_url = models.URLField(blank=True, default=settings.NOTIFY_URL)

    def __str__():
        return 'merchant urls'


# class BuyersDetail(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name_first = models.CharField(max_length=100, blank=True, default=User.first_name)
#     name_last = models.CharField(max_length=100, blank=True, default=User.last_name)
#     email = models.EmailField(max_length=100, blank=True, default=User.email, null=True)
#     cell_number = models.IntegerField(max_length=10, blank=True, default=User.phone)

#     def __str__(self):
#         return self.name_first

class TransactionDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    m_payment_id = models.CharField(max_length=120, blank=True)
    amount = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True)


# class SetPaymentMethod(models.Model):
#     payment_method = models.CharField(max_length=3, blank=True, default='cc')

#     def __str__():
#         return f'user payment type = cc'

# class RecurringBillingDetails(models.Model):
#     subscription_type = models.IntegerField(default='1')
#     recurring_amount = models.IntegerField()
#     frequency = models.IntegerField(default='3')
#     cycles = models.IntegerField(default='0')

# class SecurityFeatures(models.Model):
#     signature = models.CharField(max_length=2000, default='')    

class MyDetails(models.Model):
    merchant_id = models.CharField(max_length=200,blank=True, null=True)
    merchant_key = models.CharField(max_length=500, blank=True)

    return_url = models.URLField(blank=True, default=settings.RETURN_URL)
    cancel_url = models.URLField(blank=True, default=settings.CANCEL_URL)
    notify_url = models.URLField(blank=True, default=settings.NOTIFY_URL)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name_first = models.CharField(max_length=100, blank=True)
    name_last = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    cell_number = models.IntegerField(blank=True)

    subscription_type = models.IntegerField(default='1')
    recurring_amount = models.IntegerField()
    frequency = models.IntegerField(default='3')
    cycles = models.IntegerField(default='0')  

    # signature = models.CharField(max_length=2000, default='')   

    def __str__(self):
        return self.name_first