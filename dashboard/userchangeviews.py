from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import  (UserChangeAddressForm,
                     PasswordChangeForm,
                     ChangeNamesForm,
                     ChangeUsernameForm,
                     ChangeUsernameForm,
                     ChangePhoneForm,
                     ChangeDateBirthForm,
                     UserChangeAddressForm)


def user_change_full_names(request):
    user = get_object_or_404(User, username=request.user)
    form = ChangeNamesForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, "Full Names updated")
        return redirect('personal-info')
    else:
        messages.info(request, "could not change Names")
        return redirect('personal-info') 

def user_chage_username(request):
    user = get_object_or_404(User, username=request.user)
    form = ChangeUsernameForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, "Username Updated")
        return redirect('personal-info')
    else:
        messages.info(request, "could not change Username")
        return redirect('personal-info')

def user_chage_phone(request):
    user = get_object_or_404(User, username=request.user)
    form = ChangePhoneForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, "Phone Numbar Updated")
        return redirect('personal-info')
    else:
        messages.info(request, "could not Update Phone")
        return redirect('personal-info')       

def user_chage_date_of_birth(request):
    user = get_object_or_404(User, username=request.user)
    form = ChangeDateBirthForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, "Birth day updated")
        return redirect('personal-info')
    else:
        messages.info(request, "could not Update BirthDay")
        return redirect('personal-info')      

def user_chage_addrese(request):
    user = get_object_or_404(User, username=request.user)
    form = UserChangeAddressForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, "Address Updated")
        return redirect('personal-info')
    else:
        messages.info(request, "could not Update Addrese")
        return redirect('personal-info')   