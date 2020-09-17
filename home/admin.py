from django.contrib import admin
from .models import DesktopThumbnail, PhoneThumbnail, Logo

admin.site.register(PhoneThumbnail)
admin.site.register(DesktopThumbnail)
admin.site.register(Logo)