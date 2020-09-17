import hashlib
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import MyDetails, TransactionDetails

def cheackout_view(request):
    user = get_object_or_404(User, username=request.user.username)
    my_details = get_object_or_404(MyDetails, user=user)
    transaction_detail = TransactionDetails.objects.get(user=user)
    text = 'merchant_id={}&merchant_key={}&return_url={}&cancel_url={}&notify_url={}&m_payment_id={}&amount={}&item_name={}&item_description={}&subscription_type={}&recurring_amount={}&frequency={}&cycles={}'.format(my_details.merchant_id,my_details.merchant_key,my_details.return_url,my_details.cancel_url,my_details.notify_url,transaction_detail.m_payment_id,transaction_detail.amount,transaction_detail.item_name,transaction_detail.item_description,my_details.subscription_type,my_details.recurring_amount,my_details.frequency,my_details.cycles)
    textUtf8 = text.encode("utf-8")

    hash = hashlib.md5( textUtf8 )
    signature = hash.hexdigest()

    context = {
        'my_details': my_details,
        'signature': signature,
        'transaction_detail':transaction_detail
    }
    return render(request, 'payfast/payfast.html', context)
