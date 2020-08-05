from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from buy.models import Billing, Transaction
from .extras import generate_billing_id
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import stripe

stripe.api_key = ''

# Create your views here.
def get_user_billing(request):
    # get order for the correct user
    user = get_object_or_404(User, username=request.user.username)
    billing_user = Billing.objects.filter(User=user, is_active=True)
    if billing_user.exists():
        # get the only billing_user in the list of filtered orders
        return billing_user[0]
    return 0


def payment(request):

	return render(request, 'payment/payment.html')


def charge(request):
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user)

    if request.method == 'POST':
        token = request.POST.get('stripeToken', False)
        user_billing = get_user_billing(request)

        customer = stripe.Customer.create(
            email=user_billing.User.email,
            name=user_billing.User.username,
            source=token
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=100*user_billing.ammount,
            currency='zar',
            description=user_billing.plan
        )

    return redirect(reverse('update_records', kwargs={'token': token}))

@login_required()
def update_transaction_records(request, token):
    user = get_object_or_404(User, username=request.user.username)
    user_billing = get_user_billing(request)
    # create a transaction
    transaction = Transaction(user=user,
                            token=token,
                            billing_id=generate_billing_id(),
                            amount=user_billing.get_monthly_ammount(),
                            success=True)
    # save the transcation (otherwise doesn't exist)
    transaction.save()


    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    return redirect(reverse('dashboard'))

def password_verification(request):
    user = get_object_or_404(User, username=request.user.username)
    if request.method == 'POST':
        password = request.POST['password']
        if password == user.password:
            return redirect('canclell')
            
    return redirect('subscriptions-detail', id=user.id)        