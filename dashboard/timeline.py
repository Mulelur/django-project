from django.shortcuts import redirect, render, get_object_or_404

from .models import TimeLine
from .models import User

def Set_up_payment_method_done(request):
    user = get_object_or_404(User, username=request.user)
    # timeline =  get_object_or_404(TimeLine, user=user)
    timeline = TimeLine(user=user, set_up_payment_method='complited')

    return redirect()