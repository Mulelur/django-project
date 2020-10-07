from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Plan, Request, Billing

class PlanModelForm(ModelForm):
    class Meta: 
        model = Plan
        fields =  ['plan',]  

class RequestModelForm(ModelForm):
    class Meta:
        model = Request
        fields = ['store_name','type_of_webSite_you_want', 'a_short_description_of_your_website']

class BillingModelForm(ModelForm):
    class Meta:
        model = Billing
        fields = ['plan', 'billed_monthly', 'free_trial']

        widgets = {
            'billed_monthly': forms.CheckboxInput(attrs={'class': 'custom-control-input','checked' :'', 'id':'activity-log-1'}),
            'free_trial': forms.CheckboxInput(attrs={'class': 'custom-control-input','checked' :'', 'id':'activity-log-2'}),
            'plan' : forms.Select(attrs={'class': 'form-control'})
        }
        

class AoutoRenewOnForm(ModelForm):
    class Meta:
        model = Billing
        fields = ['auto_renew',]    

        widgets = {
            'auto_renew': forms.CheckboxInput(attrs={'class': 'custom-control-input','checked' :'', 'id':'activity-log'})
        }        

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

class BillingInfoAbbreseForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone','date_of_birth','addres_line_1', 'addres_line_2', 'city','country', 'province_or_sate', 'postal_code','currency']

        widgets = {
            'country': forms.Select(attrs={'class': 'form-select form-control form-control-lg', 'data-search': 'on'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control date-picker', 'data-date-format':'yyyy-mm-dd'})
        }
        
            
