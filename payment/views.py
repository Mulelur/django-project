from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from buy.models import Billing, Transaction
from .extras import generate_billing_id
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import stripe

stripe.api_key = 'sk_test_51HAWgTBS3gHcJ75FwIt0BQGTCNB9qGsLSAZPI189fFRhz6BY0rXgCSYZsGf7D7cSY9srpaqyFnqf1F7CRQjg1iRs00yqkz8eEw'

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


def create_plan(request):
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user)

    if request.method == 'POST':
        token = request.POST.get('stripeToken', False)
        user_billing = get_user_billing(request)

        customer = stripe.Customer.create(
            email=user_billing.User.email,
            name=user_billing.User.username,
            address={
                "line1": user_billing.addres_line_2,
                "city": user_billing.city,
                "country": user_billing.country,
                "line2": user_billing.addres_line_2,
                "postal_code": user_billing.postal_code,
                "state": user_billing.province_or_sate,
            },
            source=token
        )
        product = stripe.Product.create(
            name=user_billing.plan
        )

        if user_billing.billed_monthly:
            recurring_value="month",
        else:
            recurring_value="year", 

        price = stripe.Price.create(
            unit_amount=user_billing.ammount*100,
            currency=user_billing.country,
            recurring={"interval": "year"}, 
            product=product,
        )
               
        stripe.Subscription.create(
            customer=customer,
            items=[
                {"price": price,},
            ],
            trial_period_days='30',
            )

    return redirect(reverse('update_records', kwargs={'token': token}))

def cancel_plan(request):
    user = get_object_or_404(User, username=request.user.username)
    billing = Billing.objects.filter(User=user)

    if request.method == 'POST':
        user_billing = get_user_billing(request)
        subscription_id = stripe.Subscription.object.id
        cancel_subscription = stripe.Subscription.delete(subscription_id)

    return redirect(reverse('update_record', kwargs={'id': id}))

@login_required
def update_transaction_records(request, token):
    user = get_object_or_404(User, username=request.user.username)
    user_billing = get_user_billing(request)
    # create a transaction
    transaction = Transaction(user=user,
                            # subscription_id=id,
                            token=token,
                            billing_id=generate_billing_id(),
                            amount=user_billing.get_monthly_ammount(),
                            success=True,
                            status='active')
    # save the transcation (otherwise doesn't exist)
    transaction.save()


    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    return redirect(reverse('thank_you'))


        