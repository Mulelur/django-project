from django.forms import ModelForm
from accounts.models import Profile
from django.contrib.auth.models import User
from .models import Plan, Request, Billing

class PlanModelForm(ModelForm):
    class Meta: 
        model = Plan
        fields =  ['plan', 'free_trial',]  

class RequestModelForm(ModelForm):
    class Meta:
        model = Request
        fields = ['type_of_webSite_you_want', 'a_short_description_of_your_website']

class BillingModelForm(ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'


