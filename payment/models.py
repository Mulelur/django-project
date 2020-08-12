from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profileuser'
    )

    # 100% discount valid until
    # discount_enddate
    # Enables certain users to use
    # Django Lessons for free for period of discount.
    # Applied only manually.
    discount_enddate = models.DateField(
        null=True,
        blank=True
    )

    pro_enddate = models.DateField(
        null=True,
        blank=True
    )

    # In case user pays via Stripe and opts for
    # subcription all
    #  * stripe_subscription_id
    #  * stripe_customer_id
    #  * stripe_product_id
    # will be stored.
    # (this allows stripe's subscription cancelation)
    stripe_subscription_id = models.CharField(
        null=True,
        blank=True,
        max_length=64,
    )

    stripe_customer_id = models.CharField(
        null=True,
        blank=True,
        max_length=64,
    )

    stripe_product_id = models.CharField(
        null=True,
        blank=True,
        max_length=64,
    )


    def __str__(self):
        return f"UserProfile(username={self.user.username})"

    @property
    def is_with_automatic_renew(self):
        if not self.stripe_subscription_id:
            return False

        return True

    def update_pro_enddate(self, some_date):
        self.pro_enddate = some_date
        self.save()

    @property
    def discount(self):
        _today = datetime.date.today()

        if not self.discount_enddate:
            return False

        if not isinstance(
            self.discount_enddate, datetime.date
        ):
            return False

        return _today < self.discount_enddate

    def is_pro_user(self):
        _today = datetime.date.today()

        if self.discount:
            return True

        # If pro_enddate is not defined, blank or null
        # user is not a PRO
        if not self.pro_enddate:
            return False

        # if PRO is set in future(user paid for PRO account)
        # means he/she is a PRO
        if _today < self.pro_enddate:
            return True
