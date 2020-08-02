from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan, Request
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import UserRegisterForm
from .forms import PlanModelForm, RequestModelForm, BillingModelForm

def buyView(request):
    pass

def buyingRegisterView(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Your Account Has Benn Created!!')
        return redirect('buy-plan')

    plan = Plan.objects.all()
    template = 'buy/buy.html'

    context = {
        'plan': plan,
        'form': form
    }

    return render(request, template, context)

@login_required
def buyingPlanView(request):
    user = get_object_or_404(User, username=request.user.username)
    plan = Plan.objects.all()
    if plan:
        plan = Plan.objects.get(user=user)
        form = PlanModelForm(request.POST or None, instance=plan)
        if form.is_valid():
            form.save()
            
            return redirect('buy-request')
    else:
        form = PlanModelForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('buy-request')        

    template = 'buy/buy-plan.html'

    context = {
        'plan': plan,
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

    plan = Plan.objects.all()
    template = 'buy/buy-plan.html'

    context = {
        'plan': plan,
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
    plan = Plan.objects.get(user=user)
    template = 'buy/buy-payment.html'

    context = {
        'plan': plan
    }

    return render(request, template, context)    