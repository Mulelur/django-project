from django.shortcuts import render
from .models import Plan, DesktopThumbnail, PhoneThumbnail

def homeView(request):
    desktop_imange = DesktopThumbnail.objects.all()
    phone_image = PhoneThumbnail.objects.all() 
    try:
        desktop_imange = DesktopThumbnail.objects.get(id='1')
    
        phone_image = PhoneThumbnail.objects.get(id='1')

        context = {
            'desktop': desktop_imange,
            'phone': phone_image
        }
    except:
        ''
        context = {}

    return render(request, 'home/index.html', context)

def pricingView(request):

    plan = Plan.objects.all()

    context = {
        'plan': plan
    }
    return render(request, 'home/pricing.html', context)    

def aboutView(request):
    return render(request, 'home/about.html')    


def serviceView(request):
    return render(request, 'home/service.html')        
