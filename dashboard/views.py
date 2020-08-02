from django.shortcuts import render, get_object_or_404
from accounts.models import Profile, WebSite, Address
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterForm, UserChangeRegisterForm, UserChangeDashboardForm, UserChangeAddressForm, PasswordChangeForm
from buy.models import Billing
from django.contrib.auth.models import User

def dashboard(request):
    template = 'dashboard/index.html'
    user = get_object_or_404(Profile, user=request.user)
    website = WebSite.objects.all()
    if website:
        website = WebSite.objects.get(user=request.user)
    context = {
        'website': website
    }
    
    return render(request, template, context)

@login_required()
def personal_info(request):
    template = 'dashboard/personal_info.html'
    profile = get_object_or_404(Profile, user=request.user)
    user = User.objects.all()
    if user:
        form = UserChangeDashboardForm(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = UserChangeDashboardForm(request.POST or None)
        if form.is_valid():
            form.save()
    address = Address.objects.filter(user=request.user)
    if address:
        addressform = UserChangeAddressForm(request.POST or None, instance=address)
        if addressform.is_valid():
            addressform.save()

    else:
        addressform = UserChangeAddressForm(request.POST or None)
        if addressform.is_valid():
            addressform.save()
    context = {
        'form': form,
        'profile': profile,
        'aform': addressform
    }
      
    return render(request, template, context)    

def billing(request):
    template = 'dashboard/billing.html'
    billing = get_object_or_404(Billing, User=request.user)


    context = {
        'billing': billing
    }
    
    return render(request, template, context) 

def settings(request):
    template = 'dashboard/settings.html'
    user = get_object_or_404(Profile, user=request.user)
    form =  PasswordChangeForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    
    return render(request, template, context)  

def notification(request):
    template = 'dashboard/notification.html'

    context = {}
    
    return render(request, template, context)      

def subscriptions(request):
    template = 'dashboard/subscriptions.html'
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user)
    context = {
        'billing': billing
    }
    
    return render(request, template, context)

def payment_hestory(request):
    template = 'dashboard/payment-hestory.html'

    context = {}
    
    return render(request, template, context)


def pricing(request):
    template = 'dashboard/pricing.html'

    context = {}
    
    return render(request, template, context) 

def invoices(request):
    template = 'dashboard/invoices.html'

    context = {}
    
    return render(request, template, context) 

def invoices_detail(request):
    template = 'dashboard/invoices_detail.html'

    context = {}
    
    return render(request, template, context) 

def support(request):
    template = 'dashboard/support.html'

    context = {}
    
    return render(request, template, context)

def faqs(request):
    template = 'dashboard/faqs.html'

    context = {}
    
    return render(request, template, context)

def contact(request):
    template = 'dashboard/contact.html'

    context = {}
    
    return render(request, template, context)