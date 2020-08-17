from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from buy.models import Billing
from .models import Notification

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    phone = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'phone', 'password1', 'password2']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )

class UserChangeRegisterForm(UserRegisterForm):
    class Meta: 
        model = User
        fields = ['username', 'date_of_birth', 'phone']

class PasswordProfileForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = (
            'password1', 'password2'
        )

class UserChangeDashboardForm(UserChangeForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    phone = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name',]
    

class UserChangeAddressForm(ModelForm):
    class Meta:
        model = User
        fields = ['addres_line_1', 'addres_line_2', 'city','country', 'province_or_sate', 'postal_code']

class ChangeNamesForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ChangeUsernameForm(ModelForm):
    class Meta:
        model = User
        fields = ['username',]  
        
              
class ChangeEmailForm(UserChangeDashboardForm):
    class Meta:
        model = User
        fields = ['email',] 

              
class ChangeDateBirthForm(ModelForm):
    class Meta:
        model = User
        fields = ['date_of_birth',] 

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control date-picker', 'data-date-format':'yyyy-mm-dd'})
        }

              
class ChangePhoneForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone',] 

class UserNotificationSettingsModelForm(ModelForm):
    class  Meta:
        model = Notification
        fields = ['unusual_activity', 'new_browser', 'sales_and_latest_news', 'features_and_updates', 'tips']

        widgets = {
            'unusual_activity': forms.CheckboxInput(attrs={'class': 'custom-control-label custom-control-label', 'for': 'customSwitch1', 'id': 'customSwitch1'})
        }