from django.shortcuts import render, redirect, get_object_or_404
from .models import Billing, Request, Plan
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PlanModelForm, RequestModelForm, ChangePlanForm, BillingUpDateStateForm, BillingModelForm, AoutoRenewOnForm, SwitchBillingCycleForm
from payment.views import get_user_billing

def buyView(request):
    pass

# def buyingRegisterView(request):
#     form = UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, f'Your Account Has Benn Created!!')
#         return redirect('buy-billing')

#     billing = Billing.objects.all()
#     template = 'buy/buy.html'

#     context = {
#         'billing': billing,
#         'form': form
#     }

#     return render(request, template, context)

@login_required
def buyingPlanView(request):
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user)
    if billing:
        billing = Billing.objects.get(User=user)
        form = BillingModelForm(request.POST or None, instance=billing)
        if form.is_valid():
            form.save()
            
            return redirect('buy-request')
    else:
        form = BillingModelForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.billed_monthly:
                if obj.plan == 'PRESONAL':
                    obj.ammount = '175'
                elif obj.plan == 'BUSINESS':
                    obj.ammount = '350'
                else: 
                    obj.ammount = '785'       
            else:
                if obj.plan == 'PRESONAL':
                    obj.ammount = '1470'
                elif obj.plan == 'BUSINESS':
                    obj.ammount = '2940'
                else: 
                    obj.ammount = '6594'
            obj.user = request.user
            obj.save()  

            return redirect('buy-request')        

    template = 'buy/buy-billing.html'

    context = {
        'billing': billing,
        'form': form
    }

    return render(request, template, context)

@login_required
def buyingFreePlanView(request, username):
    user = get_object_or_404(User, username=request.user.username)
    form = PlanModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()        
        return redirect('buy-request')

    billing = Billing.objects.all()
    template = 'buy/buy-billing.html'

    context = {
        'billing': billing,
        'form': form
    }

    return render(request, template, context)   

def buyingRequestView(request):
    user = get_object_or_404(User, username=request.user.username)
    requests = Request.objects.filter(user=user).first()
    form = RequestModelForm(request.POST or None, instance=requests)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()        
        return redirect('buy-payment')

    template = 'buy/buy-request.html'

    context = {
        'form': form
    }

    return render(request, template, context)

@login_required
def buyingPaymentView(request):
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.get(User=user)
    template = 'buy/buy-payment.html'

    context = {
        'billing': billing
    }

    return render(request, template, context)    

def auto_renew_toggel(request):
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.get(User=user)

    form = AoutoRenewOnForm(request.POST or None, instance=billing)
    if form.is_valid():
        obj = form.save(commit=False)
        if obj.auto_renew:
            obj.auto_renew = False
        else:
            obj.auto_renew = True
        obj.save()        
        return redirect('subscriptions')

    return redirect('subscriptions')  

def switch_billing_cycle(request):
    template = 'dashboard/billing.html'
    billing = get_object_or_404(Billing, User=request.user, is_active=True)
    form = SwitchBillingCycleForm(request.POST or None, instance=billing)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect('billing')
  

def update_billing(request):
    user = get_object_or_404(User, username=request.user.username)
    billing = get_object_or_404(Billing, User=request.user, is_active=True)
    # form = BillingUpDateStateForm(request.POST or None, instance = billing)
    # obj = form.save(commit=False)
    # obj.is_active = False
    # obj.save()
    form = ChangePlanForm(request.POST or None, instance=billing)
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
        obj.user = user
        obj.save()
    return redirect('billing')


