from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.urls import reverse
from .forms import UserRegisterForm, EditProfileForm, PasswordProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Account Has Benn Created! {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    template = 'account/register.html'

    context = {
        'form': form
    }
    return render(request, template, context)

@login_required
def profile(request):
    template = 'account/profile.html'

    return render(request, template)

@login_required
def my_account(request):
    template = 'account/my_account.html'

    category = Category.objects.all()
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)

    context = {
        'my_orders': my_orders,
        'categories': category,
    }

    return render(request, template, context)


def edit_profile(request):
    category = Category.objects.all()
    template = 'account/edit_profile.html'
    if request.method == 'POST':
        editform = EditProfileForm(request.POST, instance=request.user)
        passwordform = PasswordProfileForm(
            data=request.POST, user=request.user)

        if editform.is_valid() or passwordform.is_valid():
            editform.save()
            return redirect(reverse('edit_profile'))
        if passwordform.is_valid():
            passwordform.save()
            update_session_auth_hash(request, passwordform.user)
            return redirect(reverse('edit_profile'))
    else:
        passwordform = PasswordProfileForm(user=request.user)
        editform = EditProfileForm(instance=request.user)
        context = {'editform': editform, 'passwordform': passwordform,'categories': category}
        return render(request, template, context)
