from .models import MyDetails, TransactionDetails
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def extars(request):
    try:
        user = get_object_or_404(User, username=request.user)
        my_details = get_object_or_404(MyDetails, user=user)
        text = ''
        textUtf8 = text.encode("utf-8")

        hash = hashlib.md5( textUtf8 )
        signature = hash.hexdigest()
    except:
        user = None
        my_details = None
        signature = None

    transaction_detail = TransactionDetails.objects.get(user=user)
    context = {
        'my_details': my_details,
        'transaction_detail': transaction_detail,
        'signature': signature
    }
    return context
   
