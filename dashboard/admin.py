from django.contrib import admin

from .models import WebSite, NotificationSetting, Notification

admin.site.register(WebSite)
admin.site.register(Notification)
admin.site.register(NotificationSetting)