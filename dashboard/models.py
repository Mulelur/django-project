from django.db import models

class Notification(models.Model):
    unusual_activity = models.BooleanField(blank=True, default=True)
    new_browser = models.BooleanField(blank=True, default=True)

    sales_and_latest_news = models.BooleanField(blank=True, default=True)
    features_and_updates = models.BooleanField(blank=True, default=True)
    tips = models.BooleanField(blank=True, default=True)