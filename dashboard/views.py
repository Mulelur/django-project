from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from buy.models import Billing, Transaction, Plan
from django.contrib.auth.models import User
from payment.views import get_user_billing
from buy.forms import ChangePlanForm, SwitchBillingCycleForm
from article.models import FAQ, Category, FAQsCategory
from .models import WebSite, Address
from .forms import UserRegisterForm, UserChangeRegisterForm, UserChangeDashboardForm, UserChangeAddressForm, PasswordChangeForm

@login_required
def dashboard(request):
    template = 'dashboard/index.html'
    user = get_object_or_404(User, username=request.user)
    website = WebSite.objects.all()
    if website:
        website = WebSite.objects.get(user=request.user)
    context = {
        'website': website
    }
    
    return render(request, template, context)

@login_required
def personal_info(request):
    template = 'dashboard/personal_info.html'
    profile = get_object_or_404(User, username=request.user)
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
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.get(User=user, is_active=True)
    form = ChangePlanForm(instance=billing)
    form1 = SwitchBillingCycleForm(request.POST or None, instance=billing)

    # if billing.is_active:


    context = {
        'billing': billing,
        'form': form,
        'form1': form1
    }
    
    return render(request, template, context) 

def settings(request):
    template = 'dashboard/settings.html'
    user = get_object_or_404(User, username=request.user)
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
    billing = Billing.objects.filter(User=user)[:5]
    get_billing = Billing.objects.get(User=user, is_active=True)
    user_billing = get_user_billing(request)
    plan = Plan.objects.exclude(plan=user_billing.plan)

    form = ChangePlanForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        if obj.billed_monthly:
            if obj.plan_id == 2:
                obj.ammount = 175
            if obj.plan_id == 1:
                obj.ammount = 350
            if obj.plan_id == 3: 
                obj.ammount = 785       
        else:
            if obj.plan_id == 2:
                obj.ammount = 1470
            if obj.plan_id == 1:
                obj.ammount = 2940
            if obj.plan_id == 3: 
                obj.ammount = 6594
        obj.user = request.user
        obj.save()  


    context = {
        'billing': billing,
        'get_billing': get_billing,
        'plan': plan,
        'form': form
    }
    
    return render(request, template, context)

def subscriptions_detail(request, id):
    template = 'dashboard/subscriptions-detail.html'
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user)
    get_billing = Billing.objects.get(User=user, is_active=True)
    user_billing = get_user_billing(request)
    plan = Plan.objects.exclude(plan=user_billing.plan)
    transaction = Transaction.objects.filter(user=user)[:4]

    context = {
        'billing': billing,
        'get_billing': get_billing,
        'plan': plan,
        'transaction': transaction
    }
    
    return render(request, template, context)    

def payment_hestory(request):
    template = 'dashboard/payment-hestory.html'
    user = get_object_or_404(User, username=request.user.username)
    transaction = Transaction.objects.filter(user=user)

    context = {
        'transaction': transaction
    }
    
    return render(request, template, context)


def pricing(request):
    template = 'dashboard/pricing.html'

    context = {}
    
    return render(request, template, context) 

def invoices(request):
    template = 'dashboard/invoices.html'
    user = get_object_or_404(User, username=request.user.username)
    transaction = Transaction.objects.filter(user=user)

    context = {
        'transaction': transaction
    }
    
    return render(request, template, context) 

def invoices_detail(request, id):
    template = 'dashboard/invoices_detail.html'
    user = get_object_or_404(User, username=request.user.username)
    transaction = Transaction.objects.get(user=user, id=id)
    billing = Billing.objects.get(User=user, is_active=True)

    context = {
        'user': user,
        'transaction': transaction,
        'billing': billing
    }
    
    return render(request, template, context) 

def invoices_print(request, id):
    template = 'dashboard/invoices_print.html'
    user = get_object_or_404(User, username=request.user.username)
    transaction = Transaction.objects.get(user=user, id=id)
    billing = Billing.objects.get(User=user, is_active=True)

    context = {
        'billing': billing,
        'transaction': transaction
    }
    
    return render(request, template, context) 

def support(request):
    template = 'dashboard/support.html'

    context = {}
    
    return render(request, template, context)

def faqs(request):
    template = 'dashboard/faqs.html'
    faqs = FAQ.objects.all()
    faqscategory = FAQsCategory.objects.all()

    context = {
        'faqs': faqs,
        'faqscategory': faqscategory
    }
    
    return render(request, template, context)

def contact(request):
    template = 'dashboard/contact.html'

    context = {}
    
    return render(request, template, context)