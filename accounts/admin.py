from django.contrib import admin

from .models import Profile, WebSite, Address

admin.site.register(Profile)
admin.site.register(WebSite)
admin.site.register(Address)
