from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from buy.models import Billing

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
        model = Billing
        fields = '__all__' 

class ChangeNamesForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ChangeUsernameForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username',]  
        
              
class ChangeEmailForm(UserChangeDashboardForm):
    class Meta:
        model = User
        fields = ['email',] 

              
class ChangeDateBirthForm(UserChangeDashboardForm):
    class Meta:
        model = User
        fields = ['date_of_birth',] 

              
class ChangePhoneForm(UserChangeDashboardForm):
    class Meta:
        model = User
        fields = ['phone',] 