from django.shortcuts import render, redirect, get_object_or_404
from .models import Billing, Request, Plan
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PlanModelForm, BillingInfoAbbreseForm, RequestModelForm, ChangePlanForm, BillingUpDateStateForm, BillingModelForm, AoutoRenewOnForm, SwitchBillingCycleForm
from payment.views import get_user_billing
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from sendEmail.functions import send_mail

def buyView(request):
    pass


@login_required
def buyingPlanView(request):
    user = get_object_or_404(User, username=request.user.username)
    user_id = get_object_or_404(User, id=request.user.id)
    billing, created = Billing.objects.get_or_create(User=user, is_active=True)

    form = BillingModelForm(request.POST or None, instance=billing)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()  


        return redirect('buy-request')        

    template = 'buy/buy-billing.html'

    context = {
        'billing': billing,
        'form': form
    }

    return render(request, template, context)

def billingInfoView(request):
    user = get_object_or_404(User, username=request.user.username)
    try:
        billing = Billing.objects.get(User=user, is_active=True)
    except:
        billing, created = Billing.objects.get_or_create(User=user)    
    form = BillingInfoAbbreseForm(request.POST or None, instance=billing)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()        
        return redirect('buy-payment')

    template = 'buy/billing.html'

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
        return redirect('billon-info')

    template = 'buy/buy-request.html'

    context = {
        'form': form
    }

    return render(request, template, context)

@login_required
def buyingPaymentView(request):
    user = get_object_or_404(User, username=request.user.username)
    try:
        billing = Billing.objects.get(User=user, is_active=True)
    except:
        billing = Billing.objects.filter(User=user).first()
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
        form.save()
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
    
    form = ChangePlanForm(request.POST or None, instance=billing)
    if form.is_valid():
        obj = form.save(commit=False)
        if obj.billed_monthly:
            if obj.plan_id == 1:
                obj.ammount = 175
            if obj.plan_id == 2:
                obj.ammount = 350
            if obj.plan_id == 3: 
                obj.ammount = 785       
        else:
            if obj.plan_id == 1:
                obj.ammount = 1470
            if obj.plan_id == 2:
                obj.ammount = 2940
            if obj.plan_id == 3: 
                obj.ammount = 6594
        obj.user = user
        obj.save()
    return redirect('billing')


def rewnew_billing(request, id):
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.get(User=request.user, id=id)
    try:
        obj=billing
        obj.is_active = True
        obj.user = user
        obj.save()
        return redirect('rewnew_confirm')
    except:
        messages.info(request, "you can not renwe a plan wiht a active one")
    return redirect('subscriptions')


def billing_cancel_view(request):
    user = get_object_or_404(User, username=request.user.username)
    get_billing = Billing.objects.get(User=request.user, is_active=True)
    billing = Billing.objects.filter(User=user)
    form = BillingUpDateStateForm(request.POST or None, instance=get_billing)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.is_active = False
        obj.user = user
        obj.save()

        return redirect('cancel_confirm')

def thank_you(request):
    template = 'buy/thank_you.html'
    user = get_object_or_404(User, username=request.user.username)

    # Send Thank You Email  

    # send_mail(user_email=user.email, user, 'Thank you', 'You  are reviceing this email besause you have selected a plan.', 'Thank You', 'buy/mail/thank_you.html')
    
    subject, from_email, to = 'Thank you', settings.EMAIL_HOST_USER, user.email
    text_content = 'You  are reviceing this email besause you have selected a plan.'
    html_content = ('<p>Thank You <strong>{}</strong> .</p>'.format(user.username))
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [user.email])
    html_template = get_template('buy/mail/thank_you.html').render()
    msg.attach_alternative(html_template, "text/html")
    msg.send()
   
    return render(request, template)

def cancel_confirm(request):
    template = 'buy/cancel_confirm.html'
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user).first()
    context = {'billing': billing}

    subject, from_email, to = 'Cancel Confirmation', settings.EMAIL_HOST_USER, user.email
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [user.email])
    html_template = get_template('buy/mail/thank_you.html', {'user': user}).render()
    msg.attach_alternative(html_template, "text/html")
    msg.send()

    return render(request, template, context)

def rewnew_confirm(request):
    template = 'buy/rewnew_confirm.html'
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user).first()

    context = {'billing': billing}
    
    subject, from_email, to = 'Subcription Renwal', settings.EMAIL_HOST_USER, user.email
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [user.email])
    html_template = get_template('buy/mail/thank_you.html').render()
    msg.attach_alternative(html_template, "text/html")
    msg.send()
    return render(request, template, context)    

@login_required
def get_started(request):
    template = 'buy/get_started.html'
    context = {}
    return render(request, template, context)