from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from buy.models import Billing, Transaction, Plan
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from payment.views import get_user_billing
from buy.forms import ChangePlanForm, SwitchBillingCycleForm, AoutoRenewOnForm
from article.models import FAQ, Category, FAQsCategory
from .models import WebSite, Notification
from .forms import (UserRegisterForm,
                     UserChangeRegisterForm,
                     UserChangeDashboardForm,
                     UserChangeAddressForm,
                     PasswordChangeForm,
                     ChangeNamesForm,
                     ChangeUsernameForm,
                     ChangeUsernameForm,
                     UserNotificationSettingsModelForm,
                     ChangePhoneForm,
                     ChangeDateBirthForm,
                     UserChangeAddressForm,
                     ChangeUserCurrency)

@login_required
def dashboard(request):
    template = 'dashboard/index.html'
    user = get_object_or_404(User, username=request.user)
    transaction = Transaction.objects.filter(user=user)
    website = WebSite.objects.filter(user=request.user)
    try:
        billing = Billing.objects.get(User=user, is_active=True)
    except:
        messages.warning(request, 'You Canceld your Plan')
        billing = Billing.objects.filter(User=user, is_active=True) 
    context = {
        'website': website,
        'billing': billing,
        'transaction': transaction
    }
    
    return render(request, template, context)

@login_required
def personal_info(request):
    template = 'dashboard/personal_info.html'
    user = get_object_or_404(User, username=request.user.username)
    profile = get_object_or_404(User, username=request.user)

    addressform = UserChangeAddressForm(request.POST or None)
    nameform = ChangeNamesForm(request.POST or None, instance=user)
    usernameform = ChangeUsernameForm(request.POST or None)
    userphoneform = ChangePhoneForm(instance=user)
    userDateOfBirthForm = ChangeDateBirthForm(instance=user)
    userAddreseForm = UserChangeAddressForm(instance=user)
   


    context = {
        'profile': profile,
        'aform': addressform,
        'nameform': nameform,
        'usernameform': usernameform,
        'userphoeform': userphoneform,
        'userDateOfBirthForm': userDateOfBirthForm,
        'userAddreseForm': userAddreseForm
    }
      
    return render(request, template, context)  

def usernameform_View(request):
    user = get_object_or_404(User, username=request.user.username)
    usernameform = ChangeUsernameForm(request.POST or None, instance=user)
    if usernameform.is_valid:
        usernameform.save()
        return redirect('personal_info')



def billing(request):
    template = 'dashboard/billing.html'
    user = get_object_or_404(User, username=request.user.username)
    
    try:
        last_transaction = Transaction.objects.filter(user=user)[0]
        billing = Billing.objects.get(User=user, is_active=True)
    except:
        last_transaction = None
        billing = None
        messages.info(request, "No last transaction")
    
    form = ChangePlanForm(instance=billing)
    form1 = SwitchBillingCycleForm(request.POST or None, instance=billing)
    auto_form = SwitchBillingCycleForm(request.POST or None, instance=billing)
    # if billing.is_active:


    context = {
        'billing': billing,
        'form': form,
        'form1': form1,
        'auto_form': auto_form,
        'last_transaction': last_transaction
    }
    
    return render(request, template, context) 

def settings(request):
    template = 'dashboard/settings.html'
    user = get_object_or_404(User, username=request.user)
    form =  PasswordChangeForm(request.POST or None)
    currency_change_form = ChangeUserCurrency(request.POST or None, instance=user)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        'currency_change_form': currency_change_form
    }
    
    return render(request, template, context)  

def notification(request):
    template = 'dashboard/notification.html'
    user = get_object_or_404(User, username=request.user)
    try:
        notification = Notification.objects.get(user=user)
        form = UserNotificationSettingsModelForm(request.POST or None, instance=notification)
        if form.is_valid():
            form.save()

    except:
        form = UserNotificationSettingsModelForm(request.POST or None)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    
    return render(request, template, context)      

def subscriptions(request):
    template = 'dashboard/subscriptions.html'
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user)[:5]
    try:
        get_billing = Billing.objects.get(User=user, is_active=True)
    except:
        get_billing = Billing.objects.filter(User=user).first()
    user_billing = get_user_billing(request)
    # plan = Plan.objects.exclude(plan=user_billing.plan)
    form_renew = AoutoRenewOnForm(instance=get_billing)
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
        # 'plan': plan,
        'form': form,
        'form_renew': form_renew
    }
    
    return render(request, template, context)

def subscriptions_detail(request, id):
    template = 'dashboard/subscriptions-detail.html'
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user)
    try:
        get_billing = Billing.objects.get(User=user, is_active=True)
    except:
        get_billing = Billing.objects.get(User=user, id=id)   
    user_billing = get_user_billing(request)
    transaction = Transaction.objects.filter(user=user)[:4]

    context = {
        'billing': billing,
        'get_billing': get_billing,
        'transaction': transaction
    }
    
    return render(request, template, context)    

def payment_hestory(request):
    template = 'dashboard/payment-hestory.html'
    user = get_object_or_404(User, username=request.user.username)
    transaction = Transaction.objects.filter(user=user)

    paginator = Paginator(transaction, 10) 
    query = request.GET.get('page')

    page_obj = paginator.get_page(query)
    context = {
        'transaction': transaction,
        'page_obj': page_obj
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
    paginator = Paginator(transaction, 10) 
    query = request.GET.get('page')

    page_obj = paginator.get_page(query)
    context = {
        'transaction': transaction,
        'page_obj':page_obj
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
    category = Category.objects.all()

    paginator = Paginator(category, 10) 
    query = request.GET.get('page')

    page_obj = paginator.get_page(query)
    context = {
        'category': category,
        'page_obj': page_obj
    }
    
    return render(request, template, context)

def faqs(request):
    template = 'dashboard/faqs.html'
    faqs = FAQ.objects.all()
    faqscategory = FAQsCategory.objects.all()
    # pagination
    paginator = Paginator(faqs, 10) 
    query = request.GET.get('page')

    page_obj = paginator.get_page(query)

    context = {
        'faqs': faqs,
        'faqscategory': faqscategory,
        'page_obj': page_obj
    }
    
    return render(request, template, context)

def contact(request):
    template = 'dashboard/contact.html'

    context = {}
    
    return render(request, template, context)

