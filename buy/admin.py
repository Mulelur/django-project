from django.contrib import admin

from .models import Plan, Request, Billing, Transaction

admin.site.register(Plan)
admin.site.register(Request)
admin.site.register(Billing)
admin.site.register(Transaction)


