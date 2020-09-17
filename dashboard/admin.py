from django.contrib import admin

from .models import WebSite, Notification, BuildDashboard, TimeLine

admin.site.register(WebSite)
admin.site.register(Notification)
admin.site.register(BuildDashboard)
admin.site.register(TimeLine)
