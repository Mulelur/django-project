from django.shortcuts import render
from .models import Plan, DesktopThumbnail, PhoneThumbnail
from home.pricing.try_web import TryWebEigth

def homeView(request):
    # try:
    desktop_imange = DesktopThumbnail.objects.get(id='1')

    phone_image = PhoneThumbnail.objects.get(title='phone-1')

    context = {
        'desktop': desktop_imange,
        'phone': phone_image
    }
    return render(request, 'home/index.html', context)

    

def pricingView(request):

    plan = Plan.objects.all()
    try_web = TryWebEigth()

    context = {
        'plan': plan,
        'try': try_web
    }
    return render(request, 'home/pricing.html', context)    

def aboutView(request):
    return render(request, 'home/about.html')    


def serviceView(request):
    return render(request, 'home/service.html')        
