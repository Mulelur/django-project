from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Plan, Request, Billing

class PlanModelForm(ModelForm):
    class Meta: 
        model = Plan
        fields =  ['plan',]  

class RequestModelForm(ModelForm):
    class Meta:
        model = Request
        fields = ['type_of_webSite_you_want', 'a_short_description_of_your_website']

class BillingModelForm(ModelForm):
    class Meta:
        model = Billing
        fields = ['plan', 'billed_monthly', 'free_trial']

class AoutoRenewOnForm(ModelForm):
    class Meta:
        model = Billing
        fields = ['auto_renew',]    

class ChangePlanForm(ModelForm):
    class Meta:
        model = Billing
        fields = ['plan', 'billed_monthly']      


class SwitchBillingCycleForm(ModelForm):
    class Meta:
        model = Billing
        fields = ['billed_monthly']         



class BillingUpDateStateForm(ModelForm):
    class Meta:
        model = Billing
        fields = ['is_active']


